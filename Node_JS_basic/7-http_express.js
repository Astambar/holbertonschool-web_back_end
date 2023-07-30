const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const filePath = process.argv[2];
const PORT = 1245;

// Route pour la page d'accueil
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route pour afficher la liste des étudiants
app.get('/students', (req, res) => {
  res.write('This is the list of our students\n');
  countStudents(filePath)
    .then((data) => {
      res.write(data.join('\n'));
      res.end();
    })
    .catch(() => {
      res.end('Cannot load the database');
    });
});

// Lancement du serveur
app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`);
});

module.exports = app;
