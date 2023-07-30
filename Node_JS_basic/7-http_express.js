// 7-http_express.js

const express = require('express');
const fs = require('fs');
const countStudents = require('./3-read_file_async');

// Vérifier si le nom de la base de données est passé en argument
if (process.argv.length !== 3) {
  console.error('Usage: node 7-http_express.js <database.csv>');
  process.exit(1);
}

const database = process.argv[2];

// Créer une instance d'Express
const app = express();

// Configuration du serveur HTTP
const PORT = 1245;

// Route pour l'URL /
app.get('/', (req, res) => {
  // Répondre avec "Hello Holberton School!" pour l'URL /
  res.send('Hello Holberton School!\n');
});

// Route pour l'URL /students
app.get('/students', (req, res) => {
  // Lire le contenu du fichier 3-read_file_async.js de manière asynchrone
  fs.readFile('./3-read_file_async.js', 'utf8', (err, data) => {
    if (err) {
      // En cas d'erreur lors de la lecture du fichier
      res.status(500).send('Internal Server Error\n');
    } else {
      // En cas de succès, afficher le message suivi du contenu du fichier 3-read_file_async.js
      res.send(`This is the list of our students\n${data}`);
    }
  });
});

// Route pour toutes les autres URL
app.use((req, res) => {
  // Répondre avec une erreur 404 et un message d'erreur pour toutes les autres URL
  res.status(404).send('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Error</title></head><body><pre>Cannot GET ' + req.url + '</pre></body></html>');
});

// Écouter le serveur sur le port spécifié
app.listen(PORT, () => {
  console.log('Server listening on port ' + PORT);
});

// Exporter le serveur pour pouvoir l'utiliser dans d'autres fichiers
module.exports = app;
