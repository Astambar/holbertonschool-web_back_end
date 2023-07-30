// Fichier : 8-clean_set.js

// La fonction cleanSet retourne une chaîne de caractères contenant toutes les valeurs
// de l'ensemble qui commencent par une chaîne spécifique.
function cleanSet(set, string) {
    // Crée une chaîne de caractères pour stocker les valeurs filtrées
    let filteredValues = '';
  
    // Parcourt chaque élément de l'ensemble
    for (const value of set) {
      // Vérifie si l'élément commence par la chaîne spécifiée
      if (value && value.startsWith(string)) {
        // Si oui, ajoute le reste de la chaîne (après string) à filteredValues
        filteredValues += filteredValues.length === 0 ? value.slice(string.length) : '-' + value.slice(string.length);
      }
    }
  
    // Renvoie les valeurs filtrées sous forme d'une chaîne de caractères
    return filteredValues;
  }
  
  // Exporte la fonction cleanSet pour pouvoir l'utiliser dans d'autres fichiers.
  export default cleanSet;
  
