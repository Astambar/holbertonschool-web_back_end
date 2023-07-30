// Fichier : 1-get_list_student_ids.js

// La fonction getListStudentIds prend un tableau d'objets en argument et retourne un tableau d'ids.
// Si l'argument n'est pas un tableau, elle retourne un tableau vide.
function getListStudentIds(studentList) {
  // Vérifie si l'argument est bien un tableau
  if (!Array.isArray(studentList)) {
    return [];
  }

  // Utilise la fonction map pour extraire les ids de chaque objet dans le tableau.
  const ids = studentList.map((student) => student.id);

  return ids;
}

// Exporte la fonction getListStudentIds pour pouvoir l'utiliser dans d'autres fichiers.
export default getListStudentIds;
