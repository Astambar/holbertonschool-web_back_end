// Fichier : 4-update_grade_by_city.js

// La fonction updateStudentGradeByCity prend en argument
// une liste d'étudiants (un tableau d'objets),
// une ville (une chaîne de caractères) et une liste de nouvelles notes (un tableau d'objets).
// Elle retourne un nouveau tableau contenant les étudiants
// de la ville spécifiée avec leurs nouvelles notes mises à jour.
function updateStudentGradeByCity(studentList, city, newGrades) {
  // Utilise la fonction filter pour filtrer les étudiants par leur lieu (attribut location).
  const studentsInCity = studentList.filter((student) => student.location === city);

  // Utilise la fonction map pour mettre à jour les notes (grades) des étudiants dans la ville.
  const updatedStudents = studentsInCity.map((student) => {
    const newGrade = newGrades.find((grade) => grade.studentId === student.id);
    return {
      ...student,
      grade: newGrade ? newGrade.grade : 'N/A',
    };
  });

  return updatedStudents;
}

// Exporte la fonction updateStudentGradeByCity pour pouvoir l'utiliser dans d'autres fichiers.
export default updateStudentGradeByCity;
