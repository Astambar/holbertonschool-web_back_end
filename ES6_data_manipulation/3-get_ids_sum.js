// Fichier : 3-get_ids_sum.js

// La fonction getStudentIdsSum prend en argument une liste d'étudiants (un tableau d'objets)
// et retourne la somme de tous les identifiants (attribut id).
// Elle utilise la fonction reduce pour réduire la liste à une seule valeur,
// qui est la somme des identifiants.
function getStudentIdsSum(studentList) {
  // Utilise la fonction reduce pour calculer la somme des identifiants des étudiants.
  const sumOfIds = studentList.reduce((accumulator, student) => accumulator + student.id, 0);

  return sumOfIds;
}

// Exporte la fonction getStudentIdsSum pour pouvoir l'utiliser dans d'autres fichiers.
export default getStudentIdsSum;
