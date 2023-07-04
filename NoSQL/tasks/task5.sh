#!/bin/bash

# Nettoyage de la base de données
mongo my_db --eval "db.dropDatabase()" > /dev/null

# Ajout de documents supplémentaires pour le test
mongo my_db --eval "db.school.insert({\"name\":\"Holberton school\"})" > /dev/null
mongo my_db --eval "db.school.insert({\"name\":\"Another school\"})" > /dev/null

# Exécution du script 5-count et stockage du résultat dans un fichier temporaire
temp_file=$(mktemp)
cat 5-count | mongo my_db > "$temp_file"

# Lecture du contenu du fichier temporaire dans une variable
result=$(cat "$temp_file")

# Motif attendu pour le nombre de documents
expected_pattern="3"

# Vérification si le résultat correspond au motif attendu
if [[ $result == *"$expected_pattern"* ]]; then
  echo "Le script affiche correctement le nombre de documents."
else
  echo "Le script n'affiche pas correctement le nombre de documents."
  exit 1
fi

# Suppression du fichier temporaire
rm "$temp_file"
