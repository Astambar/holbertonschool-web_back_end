// 4-http.js

const http = require('http');

// Création du serveur HTTP
const app = http.createServer((req, res) => {
  // Définir l'en-tête de la réponse avec le code 200 (OK) et le type de contenu en texte brut
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  // Répondre avec le message "Hello Holberton School!"
  res.end('Hello Holberton School!\n');
});

// Écouter le serveur sur le port 1245
app.listen(1245, () => {
  console.log('Server listening on port 1245');
});

// Exporter le serveur pour pouvoir l'utiliser dans d'autres fichiers
module.exports = app;
