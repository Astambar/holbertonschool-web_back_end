#!/bin/bash

# Ajouter la clé de signature publique de MongoDB
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -

# Ajouter le référentiel MongoDB
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

# Mettre à jour la liste des packages
sudo apt-get update

# Installer MongoDB
sudo apt-get install -y mongodb-org

# Vérifier le statut du service MongoDB
sudo service mongod status

sudo apt-get install jq
