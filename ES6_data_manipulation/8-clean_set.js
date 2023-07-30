// Fichier : 8-clean_set.js

// La fonction cleanSet retourne une chaîne de caractères contenant toutes les valeurs de l'ensemble qui commencent par une chaîne spécifique.
function cleanSet(set, startString) {
	// Crée un tableau pour stocker les valeurs filtrées
	const filteredValues = [];
  
	// Parcourt chaque élément de l'ensemble
	for (const value of set) {
	  // Vérifie si l'élément commence par la chaîne spécifiée
	  if (value.startsWith(startString)) {
		// Si oui, ajoute le reste de la chaîne (après startString) au tableau
		filteredValues.push(value.slice(startString.length));
	  }
	}
  
	// Renvoie le tableau sous forme d'une chaîne de caractères, en les séparant par le caractère '-'
	return filteredValues.join('-');
  }
  
  // Exporte la fonction cleanSet pour pouvoir l'utiliser dans d'autres fichiers.
  export default cleanSet;
  