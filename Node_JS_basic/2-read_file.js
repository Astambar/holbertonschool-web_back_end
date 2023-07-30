// 2-read_file.js

const fs = require('fs');

function countStudents(filePath) {
  try {
    // Lecture synchrone du fichier CSV
    const data = fs.readFileSync(filePath, 'utf8');

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
      const [firstName, lastName, age, field] = line.split(',');
      if (field === 'CS') {
        csStudents++;
        csStudentNames.push(firstName.trim()); // Utiliser trim() pour supprimer les espaces autour du nom
      } else if (field === 'SWE') {
        sweStudents++;
        sweStudentNames.push(firstName.trim()); // Utiliser trim() pour supprimer les espaces autour du nom
      }
    });

    // Afficher le nombre total d'étudiants
    console.log(`Number of students: ${numberOfStudents -1}`);

    // Afficher le nombre d'étudiants dans chaque domaine et la liste des prénoms associée
    console.log(`Number of students in CS: ${csStudents}. List: ${csStudentNames.join(', ')}`);
    console.log(`Number of students in SWE: ${sweStudents}. List: ${sweStudentNames.join(', ')}`);

  } catch (error) {
    // Gérer l'erreur si le fichier n'est pas disponible
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
