/* eslint-disable jest/require-hook */

// Affiche le nom de l'utilisateur
function displayUserName(name) {
    process.stdout.write(`Your name is: ${name}`);
  }
  
  // Gère l'entrée de l'utilisateur
  function processUserInput() {
    process.stdin.on('readable', () => {
      const name = process.stdin.read();
      if (name !== null) {
        displayUserName(name);
      }
    });
  }
  
  // Affiche le message de bienvenue
  function displayWelcomeMessage() {
    console.log('Welcome to Holberton School, what is your name?');
  }
  
  // Affiche un message de fermeture et termine le programme
  function closeProgram() {
    process.stdout.write('This important software is now closing\n');
    process.exit();
  }
  
  // Fonction principale pour demander le nom à l'utilisateur
  function askName() {
    // Étape 1 : Affiche le message de bienvenue
    displayWelcomeMessage();
  
    // Étape 2 : Écoute les événements pour gérer l'entrée de l'utilisateur
    processUserInput();
  
    // Étape 3 : Écoute l'événement 'end' pour gérer la fermeture de l'entrée standard
    process.stdin.on('end', closeProgram);
  }
  
  // Appelle la fonction pour poser la question dès que le programme démarre
  askName();
  