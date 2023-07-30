// 3-read_file_async.js

const fs = require('fs');

function countStudents(filePath) {
  return new Promise((resolve, reject) => {
    // Lecture asynchrone du fichier CSV
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        // Gérer l'erreur si le fichier n'est pas disponible
        reject(new Error('Cannot load the database'));
      } else {
        // Séparation des lignes du fichier en un tableau
        const lines = data.split('\n').filter((line) => line.trim() !== ''); // Ignorer les lignes vides

        // Calcul du nombre total d'étudiants
        const numberOfStudents = lines.length;

        // Initialisation des compteurs pour chaque domaine
        let csStudents = 0;
        let sweStudents = 0;

        // Tableaux pour stocker les prénoms des étudiants par domaine
        const csStudentNames = [];
        const sweStudentNames = [];

        // Parcourir chaque ligne et compter les étudiants dans chaque domaine
        lines.forEach((line) => {
          const [firstName, lastName, field] = line.split(',');
          if (field === 'CS') {
            csStudents++;
            csStudentNames.push(firstName);
          } else if (field === 'SWE') {
            sweStudents++;
            sweStudentNames.push(firstName);
          }
        });

        // Afficher le nombre total d'étudiants
        console.log(`Number of students: ${numberOfStudents}`);

        // Afficher le nombre d'étudiants dans chaque domaine et la liste des prénoms associée
        console.log(`Number of students in CS: ${csStudents}. List: ${csStudentNames.join(', ')}`);
        console.log(`Number of students in SWE: ${sweStudents}. List: ${sweStudentNames.join(', ')}`);

        // Résoudre la promesse après avoir effectué les opérations
        resolve();
      }
    });
  });
}

module.exports = countStudents;
