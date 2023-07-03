#!/bin/bash

# Exécution du script
result=$(cat 1-use_or_create_database | mongo 2>&1)

# Vérification du résultat
if [[ $result == *"switched to db my_db"* ]]; then
  echo "Le script a créé ou utilisé avec succès la base de données my_db."
else
  echo "Le script n'a pas créé ou utilisé correctement la base de données my_db."
fi
