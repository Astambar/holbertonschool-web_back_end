// 1-stdin.js

// Fonction pour afficher le message et attendre l'entrée de l'utilisateur
function askName() {
    process.stdout.write('Welcome to Holberton School, what is your name?\n');
  }
  
  // Événement pour lire l'entrée de l'utilisateur
  process.stdin.on('data', (data) => {
    const input = data.toString().trim();
  
    // Si l'entrée est vide, affiche le message de fermeture et termine le programme
    if (input === '') {
      console.log('This important software is now closing');
      process.exit();
    }
  
    // Sinon, affiche le nom saisi par l'utilisateur
    console.log(`Your name is: ${input}`);
    process.exit();
  });
  
  // Appelle la fonction pour poser la question dès que le programme démarre
  askName();
  