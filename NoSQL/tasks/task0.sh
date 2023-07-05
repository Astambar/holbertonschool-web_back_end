#!/bin/bash

# Exécuter le script 0-list_databases et stocker le résultat dans une variable
result=$(cat 0-list_databases | mongo)

# Définir le motif attendu
expected_pattern="admin.*0.000GB
config.*0.000GB
local.*0.000GB
my_db.*0.000GB"

# Vérifier si le résultat correspond au motif attendu
if [[ $result =~ $expected_pattern ]]; then
  echo "Le script 0-list_databases renvoie le résultat attendu :"
  echo "$result"
  exit 0  # Succès
else
  echo "Le script 0-list_databases ne renvoie pas le résultat attendu."
  echo "$result"
  exit 1  # Échec
fi
