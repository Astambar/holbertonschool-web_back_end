#!/bin/bash

# Exécution du script
result=$(cat 6-update | mongo my_db 2>&1)

# Vérification de la création de la collection "school" si elle n'existe pas
if [[ $result == *"ns not found"* ]]; then
  echo "La collection 'school' n'existe pas. Création de la collection..."
  mongo my_db --eval 'db.createCollection("school")'
fi

# Ajout d'un document de test avec name="Holberton school" si aucun document ne correspond
match_result=$(cat 4-match | mongo my_db 2>&1)
expected_result="\"name\" : \"Holberton school\""

if [[ $match_result != *"$expected_result"* ]]; then
  echo "Aucun document avec name=\"Holberton school\" trouvé. Ajout d'un document de test..."
  mongo my_db --eval 'db.school.insert({ "name" : "Holberton school" })'
fi

# Exécution du script après la création du document de test
result=$(cat 6-update | mongo my_db 2>&1)

# Résultat attendu
expected_output="WriteResult({ \"nMatched\" : 1, \"nUpserted\" : 0, \"nModified\" : 1 })"

# Vérification de l'ajout de l'attribut "address"
if [[ $result == *"$expected_output"* ]]; then
  echo "Le script a correctement ajouté l'attribut \"address\" au document."
else
  echo "Le script n'a pas ajouté correctement l'attribut \"address\" au document."
  exit 1  # Condition d'échec explicite
fi

# Vérification du document mis à jour avec l'attribut "address"
match_result=$(cat 4-match | mongo my_db 2>&1)
expected_result="\"name\" : \"Holberton school\", \"address\" : \"972 Mission street\""

if [[ $match_result == *"$expected_result"* ]]; then
  echo "Le document a été correctement mis à jour avec l'attribut \"address\"."
else
  echo "Le document n'a pas été correctement mis à jour avec l'attribut \"address\"."
  exit 1  # Condition d'échec explicite
fi
