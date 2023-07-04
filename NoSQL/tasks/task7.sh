# Exécuter une commande MongoDB pour vérifier si le document existe
document_exists=$(mongo my_db --quiet --eval 'db.collection.find({"name": "Holberton school"}).count()')

# Vérifier si le document existe
if [ "$document_exists" -eq 0 ]; then
  # Le document n'existe pas, le régénérer
  mongo my_db --quiet --eval 'db.collection.insertOne({"name": "Holberton school", "data": "sample data"})'
fi

# Exécuter le script 7-delete et stocker le résultat dans une variable
result=$(cat 7-delete | mongo my_db)

# Vérifier si le résultat contient le nombre de documents supprimés
if [[ $result == *"\"deletedCount\" : 1"* ]]; then
  echo "Le script 7-delete a supprimé le document avec name=\"Holberton school\"."
  exit 0  # Succès
else
  echo "Le script 7-delete n'a pas supprimé le document avec name=\"Holberton school\"."
  exit 1  # Échec
fi
