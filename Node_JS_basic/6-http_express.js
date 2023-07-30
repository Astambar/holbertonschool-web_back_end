const express = require('express');

const PORT = 1245;
const app = express();
module.exports = app;

// Route pour la page d'accueil
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Lancement du serveur
app.listen(PORT, () => {
  console.log(`Le serveur écoute sur le port ${PORT}`);
});
