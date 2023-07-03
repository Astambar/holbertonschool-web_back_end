#!/bin/bash

# Exécution du script
result=$(cat 2-insert | mongo my_db 2>&1)

# Vérification du résultat
if [[ $result == *"WriteResult({ \"nInserted\" : 1 })"* ]]; then
  echo "Le script a inséré avec succès le document dans la collection school."
else
  echo "Le script n'a pas inséré correctement le document dans la collection school."
fi
