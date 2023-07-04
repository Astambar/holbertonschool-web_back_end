#!/bin/bash

# Exécuter le script 9-main.py et stocker la sortie dans une variable
result=$(python3 9-main.py)

# Vérifier si la sortie contient le message "New school created" suivi d'un ID
if [[ $result =~ New\ school\ created:\ ([0-9a-f]+) ]]; then
  # Récupérer l'ID du document inséré
  inserted_id="${BASH_REMATCH[1]}"
  echo "L'insertion de l'école a réussi. ID du document inséré : $inserted_id"
else
  echo "L'insertion de l'école a échoué."
  exit 1  # Échec
fi

# Vérifier si le document inséré existe dans la collection
if [[ $result =~ $inserted_id.*UCSF.*505.*Parnassus.*Ave ]]; then
  # Le document inséré existe dans la collection
  echo "Le document inséré existe dans la collection."
  echo "Résultat: $result"
  exit 0  # Succès
else
  # Le document inséré n'existe pas dans la collection
  echo "Le document inséré n'existe pas dans la collection."
  echo "Résultat: $result"
  exit 1  # Échec
fi
