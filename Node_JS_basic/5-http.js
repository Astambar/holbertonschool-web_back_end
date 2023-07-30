// Importation du module HTTP requis pour créer un serveur
const http = require('http');

// Importation de la fonction countStudents depuis le fichier '3-read_file_async.js'
const countStudents = require('./3-read_file_async');

// Définition de l'adresse IP et du port sur lesquels le serveur va écouter
const hostname = '127.0.0.1';
const port = 1245;

// Récupération du nom de la base de données depuis les arguments de ligne de commande
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
    // Appel de la fonction countStudents pour obtenir les données des étudiants depuis la base de données
    const studentsData = await countStudents(DB);
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.write('This is the list of our students\n');
    res.end(studentsData.join('\n')); // Envoi de la liste des étudiants au format texte avec un saut de ligne entre chaque nom
  } catch (error) {
    // En cas d'erreur lors de l'accès à la base de données, renvoyer une réponse d'erreur avec le code 500
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
  // Vérification de l'URL de la requête pour déterminer quelle fonction de gestion de route utiliser
  if (req.url === '/') {
    handleRootRoute(req, res); // Gérer la route racine
  } else if (req.url === '/students') {
    handleStudentsRoute(req, res); // Gérer la route '/students'
  } else {
    handleNotFound(req, res); // Gérer les autres routes avec une réponse '404 Not Found'
  }
});

// Démarrer le serveur et écouter sur le port et l'adresse IP spécifiés
app.listen(port, hostname, () => {
  console.log('Server running at localhost:1245');
});

// Exporter la variable 'app' pour pouvoir l'utiliser dans d'autres fichiers
module.exports = app;
