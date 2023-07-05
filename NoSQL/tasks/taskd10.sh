#!/bin/bash

# Exécuter le script 10-main.py et stocker la sortie dans une variable
result=$(python3 10-main.py)

# Extraire le nom de l'école à partir de la sortie
school_name=$(grep -oP '\[[^ ]+' <<< "$result" | tr -d '[]')
echo $school_name
# Vérifier si les informations de l'école ont été mises à jour correctement
if [[ "$result" =~ "$school_name.*\['iOS'\]" ]]; then
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
