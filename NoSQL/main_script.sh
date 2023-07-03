#!/bin/bash

# Répertoire des tâches
TASK_DIR="tasks"

# Répertoire des rapports
REPORT_DIR="reports"

# Créer le répertoire des rapports s'il n'existe pas
mkdir -p "$REPORT_DIR"

# Initialiser les compteurs de tests réussis et échoués
success_count=0
fail_count=0

# Chemin vers le fichier des rapports de succès
success_file="$REPORT_DIR/success_report.txt"
# Chemin vers le fichier des rapports d'échec
fail_file="$REPORT_DIR/fail_report.txt"

# Vider les fichiers de rapport (écrasement du contenu précédent)
> "$success_file"
> "$fail_file"

# Fonction pour exécuter un test
run_test() {
  task="$1"
  task_name=$(basename "$task")
  report_file="$REPORT_DIR/${task_name}_report.txt"

  # Exécuter le test et enregistrer le résultat dans le rapport correspondant
  if bash "$task" > "$report_file" 2>&1; then
    echo "[SUCCESS] $task"
    ((success_count++))
    echo "Test: $task" >> "$success_file"
    echo "=====================================" >> "$success_file"
    cat "$report_file" >> "$success_file"
    echo >> "$success_file"
  else
    echo "[FAIL] $task"
    ((fail_count++))
    echo "Test: $task" >> "$fail_file"
    echo "=====================================" >> "$fail_file"
    cat "$report_file" >> "$fail_file"
    echo >> "$fail_file"
  fi
}

# Liste des tâches à tester
tasks=("$TASK_DIR"/*.sh)

# Parcourir la liste des tâches et exécuter les tests
for task in "${tasks[@]}"; do
  # Vérifier si le fichier de la tâche existe
  if [ -f "$task" ]; then
    run_test "$task"
  else
    echo "[ERROR] Fichier non trouvé : $task"
  fi
done

# Afficher le résumé des résultats
echo "Résumé des résultats :"
echo "Tests réussis : $success_count"
echo "Tests échoués : $fail_count"

# Si au moins un test a échoué, le script de test principal renverra un code de sortie non nul
if ((fail_count > 0)); then
  exit 1
fi
