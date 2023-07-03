#!/bin/bash

# Exécution du script de recherche
result=$(cat 4-match | mongo my_db 2>&1)

# Premier test : Vérification de la présence d'un résultat
if [[ -n $result ]]; then
  echo "Le script a réussi à trouver quelque chose."
else
  echo "Le script n'a pas réussi à trouver quelque chose."
  exit 1  # Condition d'échec explicite
fi

# Deuxième test : Vérification du contenu du résultat
expected_name="Holberton school"
if [[ $result =~ "\"name\" : \"$expected_name\"" ]]; then
  echo "Le script liste correctement tous les documents avec name=\"$expected_name\"."
else
  echo "Le script ne liste pas correctement tous les documents avec name=\"$expected_name\"."
  exit 1  # Condition d'échec explicite
fi
