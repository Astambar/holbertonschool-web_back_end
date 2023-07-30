// Fichier : 5-typed_arrays.js

// La fonction createInt8TypedArray retourne un nouveau ArrayBuffer avec une valeur Int8 à une position spécifique.
function createInt8TypedArray(length, position, value) {
	// Vérifie si la position est valide
	if (position < 0 || position >= length) {
	  throw new Error("Position outside range");
	}
  
	// Crée un nouveau ArrayBuffer de la longueur spécifiée
	const buffer = new ArrayBuffer(length);
  
	// Crée une vue DataView pour manipuler les données du ArrayBuffer
	const view = new DataView(buffer);
  
	// Place la valeur Int8 à la position spécifiée dans le DataView
	view.setInt8(position, value);
  
	return view;
  }
  
  // Exporte la fonction createInt8TypedArray pour pouvoir l'utiliser dans d'autres fichiers.
  export default createInt8TypedArray;
  