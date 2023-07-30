// Fichier : 100-weak.js

// Exporte une constante instance de WeakMap nommée weakMap
export const weakMap = new WeakMap();

// Exporte une nouvelle fonction queryAPI qui gère le suivi des requêtes pour chaque endpoint
export function queryAPI(endpoint) {
  // Vérifie si le endpoint existe déjà dans le WeakMap
  if (weakMap.has(endpoint)) {
    // Récupère le nombre de requêtes pour ce endpoint depuis le WeakMap
    const requestCount = weakMap.get(endpoint);
    
    // Incrémente le nombre de requêtes
    weakMap.set(endpoint, requestCount + 1);

    // Vérifie si le nombre de requêtes est >= 5, et lance une erreur si c'est le cas
    if (requestCount + 1 >= 5) {
      throw new Error('Endpoint load is high');
    }
  } else {
    // Si le endpoint n'existe pas dans le WeakMap, initialise le nombre de requêtes à 1
    weakMap.set(endpoint, 1);
  }
}
