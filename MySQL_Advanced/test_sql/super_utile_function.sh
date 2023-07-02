#!/bin/bash

# Fonction pour afficher un message de réussite
function print_success() {
  echo -e "\e[32m[SUCCESS]\e[0m"
}

# Fonction pour afficher un message d'échec
function print_failure() {
  echo -e "\e[31m[FAILURE]\e[0m"
}

# Fonction pour ajouter un test réussi à la liste des tests
function add_success_test() {
  local file_name="$1"
  local test_type="$2"
  local test_name="$3"
  local test_description="$4"

  echo "- Test: $file_name"
  echo "  Type: $test_type"
  echo "  Name: $test_name"
  echo "  Description: $test_description"
  echo "  Result: \e[32mSUCCESS\e[0m"
}

# Fonction pour ajouter un test échoué à la liste des tests
function add_failure_test() {
  local file_name="$1"
  local test_type="$2"
  local test_name="$3"
  local test_description="$4"

  echo "- Test: $file_name"
  echo "  Type: $test_type"
  echo "  Name: $test_name"
  echo "  Description: $test_description"
  echo "  Result: \e[31mFAILURE\e[0m"
}

# Fonction pour créer les fichiers de récapitulatif
function create_summary_files() {
  summary_dir="test_summary"
  if [ ! -d "$summary_dir" ]; then
    mkdir "$summary_dir"
  fi

  success_file="$summary_dir/success_tests.txt"
  failure_file="$summary_dir/failure_tests.txt"

  if [ ! -f "$success_file" ]; then
    touch "$success_file"
  fi

  if [ ! -f "$failure_file" ]; then
    touch "$failure_file"
  fi
}

# Fonction pour nettoyer les fichiers temporaires
function cleanup() {
  rm -f "sql_execution_results.txt"
}

# Initialisation des variables de compte
count_success=0
count_failure=0
failed_tests=""
sql_execution_results=""
