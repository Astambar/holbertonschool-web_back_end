// Fichier : 10-update_uniq_items.js

// La fonction updateUniqueItems met à jour la quantité à 100 pour tous les éléments ayant une quantité initiale de 1 dans l'objet Map.
function updateUniqueItems(map) {
	// Vérifie si l'argument est un objet Map
	if (!(map instanceof Map)) {
	  throw new Error('Cannot process');
	}
  
	// Parcourt chaque entrée de l'objet Map
	for (const [key, value] of map.entries()) {
	  // Si la quantité est de 1, met à jour la quantité à 100
	  if (value === 1) {
		map.set(key, 100);
	  }
	}
  }
  
  // Exporte la fonction updateUniqueItems pour pouvoir l'utiliser dans d'autres fichiers.
  export default updateUniqueItems;
  