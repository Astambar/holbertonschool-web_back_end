#!/bin/bash

# Importer les fonctions de test
source test_sql/super_utile_function.sh
source test_sql/test_uniq_users.sh
source test_sql/test_country_users.sh

# Fonction pour créer le répertoire de résultats par défaut
function create_default_result_directory() {
  default_result_directory="test_results"
  if [ ! -d "$default_result_directory" ]; then
    mkdir "$default_result_directory"
  fi
}

# Fonction de test principale
function main_test() {
  # Chemin vers le dossier contenant les fichiers SQL
  SQL_DIR="."

  # Nom de la base de données
  DB_NAME="holberton"

  # Connexion à MySQL en tant que superutilisateur sans mot de passe
  MYSQL_CMD="sudo mysql -uroot"

  # Création de la base de données
  echo "Creating database $DB_NAME"
  $MYSQL_CMD -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"

  # Sélection de la base de données
  $MYSQL_CMD -e "USE $DB_NAME;"

  # Parcours de tous les fichiers SQL dans le répertoire spécifié
  for sql_file in "$SQL_DIR"/*.sql; do
    echo "Executing $sql_file"
    # Exécution du fichier SQL avec MySQL (dans un bloc try-catch)
    error_output=$($MYSQL_CMD < "$sql_file" 2>&1)
    if [ $? -eq 0 ]; then
      echo "Execution successful"
      print_success
      sql_execution_results+="\n$sql_file:\n$error_output"
      # Appeler la fonction de test correspondante
      if [[ $sql_file == *0-uniq_users.sql* ]]; then
        $MYSQL_CMD -e "USE $DB_NAME;"
        test_uniq_users "$sql_file"
        if [ $? -eq 0 ]; then
          add_success_test "$sql_file" "Integrity Test" "uniq_users" "Test Uniq Users"
        else
          add_failure_test "$sql_file" "Integrity Test" "uniq_users" "Test Uniq Users"
          ((count_failure++))
        fi
      elif [[ $sql_file == *1-country_users.sql* ]]; then
        $MYSQL_CMD -e "USE $DB_NAME;"
        test_country_users "$sql_file"
        if [ $? -eq 0 ]; then
          add_success_test "$sql_file" "Integrity Test" "country_users" "Test Country Users"
        else
          add_failure_test "$sql_file" "Integrity Test" "country_users" "Test Country Users"
          ((count_failure++))
        fi
      fi
      ((count_success++))
    else
      echo "Execution failed, rolling back"
      $MYSQL_CMD -e "ROLLBACK;" >/dev/null 2>&1
      print_failure
      sql_execution_results+="\n$sql_file:\n$error_output"
      ((count_failure++))
      failed_tests+="\n- $sql_file"
      add_failure_test "$sql_file" "Unknown Test" "Unknown Error" "$error_output"
    fi
  done

  # Afficher le nombre de tests réussis et échoués si supérieur à zéro
  if ((count_success > 0)); then
    echo "Total tests passed: $count_success"
  fi
  if ((count_failure > 0)); then
    echo -e "Total tests failed: $count_failure\nFailed tests:"
    echo -e "$failed_tests"
  fi

  # Afficher le résultat final en évidence
  echo "============================="
  if ((count_failure == 0)); then
    echo -e "\e[32mAll tests passed successfully!\e[0m"
  else
    echo -e "\e[31mSome tests failed.\e[0m"
  fi
  echo "============================="

  # Enregistrer les résultats d'exécution dans un fichier
  save_execution_results
}

# Appel de la fonction de création des fichiers de récapitulatif
create_summary_files

# Appel de la fonction de création du répertoire de résultats par défaut
create_default_result_directory

# Appel de la fonction de test principale
main_test

# Nettoyage à la fin des tests
cleanup
