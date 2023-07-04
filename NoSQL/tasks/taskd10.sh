#!/bin/bash

# Exécuter le script 10-main.py et stocker la sortie dans une variable
result=$(python3 10-main.py)

# Extraire l'ID du document de l'école à partir de la sortie
school_id=$(grep -oP '\[\K[^]]+' <<< "$result")

# Vérifier si les informations de l'école ont été mises à jour correctement
if [[ $(mongo my_db --quiet --eval "db.school.find({_id: ObjectId('$school_id'), topics: ['iOS']}).count()") == "1" ]]; then
  # Les informations de l'école ont été mises à jour
  echo "Les informations de l'école ont été mises à jour."
  echo "Résultat: $result"
  exit 0  # Succès
else
  # Les informations de l'école n'ont pas été mises à jour
  echo "Les informations de l'école n'ont pas été mises à jour."
  echo "Résultat: $result"
  exit 1  # Échec
fi
