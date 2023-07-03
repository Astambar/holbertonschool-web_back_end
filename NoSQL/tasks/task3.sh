#!/bin/bash

# Exécution du script
result=$(cat 3-all | mongo my_db 2>&1)

# Résultat attendu
expected_name="Holberton school"

# Extraire le nom du résultat effectif
actual_name=$(echo "$result" | grep -o '"name" : "[^"]*' | sed 's/"name" : "//')

# Vérification de la valeur extraite
if [[ $actual_name == "$expected_name" ]]; then
  echo "Le script liste correctement tous les documents de la collection school."
else
  echo "Le script ne liste pas correctement tous les documents de la collection school."
fi
