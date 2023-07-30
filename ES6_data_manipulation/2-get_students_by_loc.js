// Fichier : 2-get_students_by_loc.js

// La fonction getStudentsByLocation prend en argument une liste d'étudiants (un tableau d'objets) et une ville (une chaîne de caractères).
// Elle renvoie un nouveau tableau contenant uniquement les étudiants situés dans la ville spécifiée.
function getStudentsByLocation(studentList, city) {
  // Utilise la fonction filter pour filtrer les étudiants par leur lieu (attribut location).
  const studentsInCity = studentList.filter((student) => student.location === city);

  return studentsInCity;
}

// Exporte la fonction getStudentsByLocation pour pouvoir l'utiliser dans d'autres fichiers.
export default getStudentsByLocation;
