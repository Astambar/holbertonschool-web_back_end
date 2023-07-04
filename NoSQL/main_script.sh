#!/bin/bash

# Répertoire des tâches
TASK_DIR="tasks"

# Répertoire des rapports de test
REPORT_DIR="reports"

# Répertoire des tests de charge
LOAD_TEST_DIR="load_tests"

# Répertoire des rapports de charge
LOAD_REPORT_DIR="$REPORT_DIR/load_reports"

# Répertoire des rapports de charge individuels
INDIVIDUAL_LOAD_REPORT_DIR="$LOAD_REPORT_DIR/individual_reports"

# Répertoire des journaux
LOG_DIR="logs"

# Répertoire des journaux d'échec
FAILURE_LOG_DIR="$LOG_DIR/failure_logs"

# Fichier de succès des tests
success_file="$REPORT_DIR/success.txt"

# Fichier d'échec des tests
fail_file="$REPORT_DIR/fail.txt"

# Fichier de réussite des tests de charge
charge_success_file="$LOAD_REPORT_DIR/success.txt"

# Fichier d'échec des tests de charge
charge_fail_file="$LOAD_REPORT_DIR/fail.txt"

# Compteur de tests réussis
success_count=0

# Compteur de tests échoués
fail_count=0

# Compteur de tests de charge réussis
charge_success_count=0

# Compteur de tests de charge échoués
charge_fail_count=0

# Fonction pour exécuter un test
run_test() {
  task="$1"
  is_load_test="$2"

  # Nom du fichier de rapport
  report_file="${task%.*}.txt"

  # Vérifier si le rapport doit être enregistré individuellement
  if [ "$is_load_test" = true ]; then
    report_file="$INDIVIDUAL_LOAD_REPORT_DIR/$(basename "$report_file")"
  else
    report_file="$REPORT_DIR/$(basename "$report_file")"
  fi

  echo -n "Exécution du test : $task... "

  # Exécuter la tâche et enregistrer le rapport
  if bash "$task" > "$report_file" 2>&1; then
    echo -e "[\e[1;32mSUCCESS\e[0m] $task"

    # Mettre à jour les compteurs de réussite
    if [ "$is_load_test" = true ]; then
      ((charge_success_count++))
      echo -e "Test: $task" >> "$charge_success_file"
      echo -e "=====================================" >> "$charge_success_file"
      cat "$report_file" >> "$charge_success_file"
      echo >> "$charge_success_file"
    else
      ((success_count++))
      echo -e "Test: $task" >> "$success_file"
      echo -e "=====================================" >> "$success_file"
      cat "$report_file" >> "$success_file"
      echo >> "$success_file"
    fi
  else
    echo -e "[\e[1;31mFAIL\e[0m] $task"

    # Vérifier si c'est un test de charge et mettre à jour les compteurs appropriés
    if [ "$is_load_test" = true ]; then
      ((charge_fail_count++))
      echo -e "Test: $task" >> "$charge_fail_file"
      echo -e "=====================================" >> "$charge_fail_file"
      cat "$report_file" >> "$charge_fail_file"
      echo >> "$charge_fail_file"

      # Enregistrer les logs CPU et mémoire spécifiques à l'échec
      cp "$LOG_DIR/cpu.log" "$FAILURE_LOG_DIR/$(basename "$task").cpu.log"
      cp "$LOG_DIR/memory.log" "$FAILURE_LOG_DIR/$(basename "$task").memory.log"
    else
      ((fail_count++))
      echo -e "Test: $task" >> "$fail_file"
      echo -e "=====================================" >> "$fail_file"
      cat "$report_file" >> "$fail_file"
      echo >> "$fail_file"

      # Enregistrer les logs CPU et mémoire spécifiques à l'échec
      cp "$LOG_DIR/cpu.log" "$FAILURE_LOG_DIR/$(basename "$task").cpu.log"
      cp "$LOG_DIR/memory.log" "$FAILURE_LOG_DIR/$(basename "$task").memory.log"
    fi
  fi
}

# Créer les répertoires nécessaires
mkdir -p "$REPORT_DIR"
mkdir -p "$LOAD_REPORT_DIR"
mkdir -p "$INDIVIDUAL_LOAD_REPORT_DIR"
mkdir -p "$LOG_DIR"
mkdir -p "$FAILURE_LOG_DIR"

# Supprimer les anciens rapports
rm -f "$success_file" "$fail_file" "$charge_success_file" "$charge_fail_file"
rm -rf "$INDIVIDUAL_LOAD_REPORT_DIR"/*

# Parcourir les tâches et exécuter les tests
for task in "$TASK_DIR"/*.sh; do
  # Vérifier si le fichier de tâche existe
  if [ -f "$task" ]; then
    run_test "$task" false
  else
    echo -e "[\e[1;33mERROR\e[0m] Fichier non trouvé : $task"
  fi
done

# Vérifier si des tests de charge doivent être exécutés
if [ -d "$LOAD_TEST_DIR" ]; then
  # Parcourir les tests de charge et exécuter les tests
  for load_test in "$LOAD_TEST_DIR"/*.sh; do
    # Vérifier si le fichier de test de charge existe
    if [ -f "$load_test" ]; then
      # Créer un répertoire individuel pour les rapports de charge
      load_test_dir="$INDIVIDUAL_LOAD_REPORT_DIR/$(basename "${load_test%.*}")"
      mkdir -p "$load_test_dir"

      # Exécuter le test de charge
      run_test "$load_test" true

      # Déplacer les rapports de charge individuels vers le répertoire approprié
      mv "$INDIVIDUAL_LOAD_REPORT_DIR"/*.txt "$load_test_dir"
    else
      echo -e "[\e[1;33mERROR\e[0m] Fichier non trouvé : $load_test"
    fi
  done
fi

# Générer le fichier de test de charge
load_test_file="$LOAD_TEST_DIR/load.sh"

if [ ! -f "$load_test_file" ]; then
  echo "Création du fichier de test de charge : $load_test_file"

  # Générer le contenu du fichier de test de charge
  cat > "$load_test_file" <<EOF
#!/bin/bash

# Exécuter la tâche en boucle pour effectuer un test de charge
for i in {1..100}; do
  # Exécuter la tâche ici
  if bash "\$task" > /dev/null 2>&1; then
    echo "SUCCESS"
  else
    echo "FAIL"
  fi

  # Enregistrer l'utilisation du CPU
  top -b -n 1 | grep "Cpu(s)" >> "$LOG_DIR/cpu.log"

  # Enregistrer l'utilisation de la mémoire
  free -m | grep "Mem:" >> "$LOG_DIR/memory.log"
done
EOF
fi

echo -e "Rapport global :\n"
echo -e "Nombre de tests réussis : $success_count"
echo -e "Nombre de tests échoués : $fail_count"
echo -e "Rapport des tests réussis : $success_file"
echo -e "Rapport des tests échoués : $fail_file"
echo -e "====================================="

echo -e "Rapport des tests de charge :\n"
echo -e "Nombre de tests réussis : $charge_success_count"
echo -e "Nombre de tests échoués : $charge_fail_count"
echo -e "Rapport des tests réussis : $charge_success_file"
echo -e "Rapport des tests échoués : $charge_fail_file"
