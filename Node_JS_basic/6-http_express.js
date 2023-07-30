// 6-http_express.js

const express = require('express');

// Créer une instance d'Express
const app = express();

// Configuration du serveur HTTP
const PORT = 1245;

// Route pour l'URL /
app.get('/', (req, res) => {
  // Répondre avec "Hello Holberton School!" pour l'URL /
  res.send('Hello Holberton School!\n');
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
