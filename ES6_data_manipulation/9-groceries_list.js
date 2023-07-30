// Fichier : 9-groceries_list.js

// La fonction groceriesList retourne un objet Map contenant les éléments
// d'une liste d'épicerie avec leur quantité associée.
function groceriesList() {
  // Crée un nouvel objet Map
  const groceryMap = new Map();

  // Ajoute les éléments de la liste d'épicerie avec leur quantité dans le Map
  groceryMap.set('Apples', 10);
  groceryMap.set('Tomatoes', 10);
  groceryMap.set('Pasta', 1);
  groceryMap.set('Rice', 1);
  groceryMap.set('Banana', 5);

  return groceryMap;
}

// Exporte la fonction groceriesList pour pouvoir l'utiliser dans d'autres fichiers.
export default groceriesList;
