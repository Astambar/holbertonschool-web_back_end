const http = require('http');
const countStudents = require('./3-read_file_async');

const hostname = '127.0.0.1';
const port = 1245;
const DB = process.argv[2];

// Fonction pour gérer la route racine '/'
function handleRootRoute(req, res) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!');
}

// Fonction pour gérer la route '/students'
async function handleStudentsRoute(req, res) {
  try {
    const studentsData = await countStudents(DB);
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.write('This is the list of our students\n');
    res.end(studentsData.join('\n'));
  } catch (error) {
    res.statusCode = 500;
    res.setHeader('Content-Type', 'text/plain');
    res.end(`Cannot load the database: ${error.message}`);
  }
}

// Fonction pour gérer les autres routes avec une réponse '404 Not Found'
function handleNotFound(req, res) {
  res.statusCode = 404;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Not Found');
}

// Création du serveur HTTP en utilisant le module 'http'
const app = http.createServer((req, res) => {
  if (req.url === '/') {
    handleRootRoute(req, res);
  } else if (req.url === '/students') {
    handleStudentsRoute(req, res);
  } else {
    handleNotFound(req, res);
  }
});

// Démarrer le serveur et écouter sur le port et l'adresse IP spécifiés
app.listen(port, hostname, () => {
  console.log('Server running at localhost:1245');
});

// Exporter la variable 'app' pour pouvoir l'utiliser dans d'autres fichiers
module.exports = app;
