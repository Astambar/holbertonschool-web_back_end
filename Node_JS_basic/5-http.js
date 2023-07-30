// 5-http.js

const http = require('http');
const fs = require('fs');
const countStudents = require('./3-read_file_async');

// Vérifier si le nom de la base de données est passé en argument
if (process.argv.length !== 3) {
  console.error('Usage: node 5-http.js <database.csv>');
  process.exit(1);
}

const database = process.argv[2];

// Création du serveur HTTP
const app = http.createServer((req, res) => {
  if (req.url === '/') {
    // Répondre avec "Hello Holberton School!" pour l'URL /
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!\n');
  } else if (req.url === '/students') {
    // Lire le contenu du fichier 3-read_file_async.js de manière asynchrone
    fs.readFile('./3-read_file_async.js', 'utf8', (err, data) => {
      if (err) {
        // En cas d'erreur lors de la lecture du fichier
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Internal Server Error\n');
      } else {
        // En cas de succès, afficher le message suivi du contenu du fichier 3-read_file_async.js
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(`This is the list of our students\n${data}`);
      }
    });
  } else {
    // Répondre avec une erreur 404 pour toutes les autres URL
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found\n');
  }
});

// Écouter le serveur sur le port 1245
app.listen(1245, () => {
  console.log('Server listening on port 1245');
});

// Exporter le serveur pour pouvoir l'utiliser dans d'autres fichiers
module.exports = app;
