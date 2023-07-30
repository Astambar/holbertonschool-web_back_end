// Fichier : 0-get_list_students.js

// La fonction getListStudents retourne le tableau d'objets d'étudiants spécifié dans l'énoncé.
function getListStudents() {
	return [
	  { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
	  { id: 2, firstName: 'James', location: 'Columbia' },
	  { id: 5, firstName: 'Serena', location: 'San Francisco' }
	];
  }
  
  // Exporte la fonction getListStudents pour pouvoir l'utiliser dans d'autres fichiers.
  export default getListStudents;
  