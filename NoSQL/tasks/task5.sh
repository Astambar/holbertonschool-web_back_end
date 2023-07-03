#!/bin/bash

# Nettoyage de la base de données
mongo my_db --eval "db.dropDatabase()"

# Ajout de documents supplémentaires pour le test
mongo my_db --eval "db.school.insert({\"name\":\"Holberton school\"})"
mongo my_db --eval "db.school.insert({\"name\":\"Another school\"})"

# Test : Nombre de documents
result=$(cat 5-count | mongo my_db 2>&1)
expected_result="3"  # On s'attend à ce qu'il y ait 3 documents (y compris les documents supplémentaires ajoutés)

if [[ $result == *"$expected_result"* ]]; then
  echo "Le script affiche correctement le nombre de documents."
else
  echo "Le script n'affiche pas correctement le nombre de documents."
  exit 1
fi
