// Fichier : 6-set.js

// La fonction setFromArray retourne un nouvel objet Set à partir d'un tableau.
function setFromArray(arr) {
	// Crée un nouvel objet Set à partir du tableau donné.
	const set = new Set(arr);
  
	return set;
  }
  
  // Exporte la fonction setFromArray pour pouvoir l'utiliser dans d'autres fichiers.
  export default setFromArray;
  