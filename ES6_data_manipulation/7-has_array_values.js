// Fichier : 7-has_array_values.js

// La fonction hasValuesFromArray retourne un booléen indiquant si tous les éléments du tableau existent dans l'ensemble.
function hasValuesFromArray(set, arr) {
	// Vérifie si tous les éléments du tableau existent dans l'ensemble.
	for (const element of arr) {
	  if (!set.has(element)) {
		return false;
	  }
	}
  
	return true;
  }
  
  // Exporte la fonction hasValuesFromArray pour pouvoir l'utiliser dans d'autres fichiers.
  export default hasValuesFromArray;
  