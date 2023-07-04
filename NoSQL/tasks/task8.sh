#!/bin/bash

# Exécuter le script 8-main.py et stocker le résultat dans une variable
result=$(python3 8-main.py)

# Définir les motifs attendus pour chaque ligne de résultat
expected_pattern1="\[[a-z0-9]{24}\] .+"
expected_pattern2="\[[a-z0-9]{24}\] .+"

# Vérifier si chaque ligne de résultat correspond au motif attendu
if [[ $result =~ $expected_pattern1 ]] && [[ $result =~ $expected_pattern2 ]]; then
  echo "Le script 8-main.py renvoie le résultat attendu :"
  echo "$result"
  exit 0  # Succès
else
  echo "Le script 8-main.py ne renvoie pas le résultat attendu."
  exit 1  # Échec
fi
