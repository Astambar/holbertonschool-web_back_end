#!/usr/bin/env python3
"""
102-log_stats.py - Script pour analyser les statistiques
  des journaux dans une collection MongoDB.
"""
from pymongo import MongoClient

# Liste des méthodes HTTP
METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

# Pipeline pour l'agrégation des adresses IP
PIPE = [
    {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
]


def log_stats(mongo_collection, option=None):
    """
    Analyse des statistiques des journaux dans une collection MongoDB.
    :param mongo_collection: Objet de collection MongoDB
    :param option: Paramètre optionnel pour filtrer
       les journaux par méthode HTTP
    """
    if option:
        # Compter le nombre de journaux pour une méthode HTTP spécifique
        value = mongo_collection.count_documents(
                                                  {
                                                      "method":
                                                          {
                                                              "$regex": option
                                                          }
                                                  }
                                                 )
        print(f"\tméthode {option}: {value}")
        return

    # Nombre total de journaux
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} journaux")

    print("Méthodes :")
    for method in METHODS:
        log_stats(mongo_collection, method)

    # Compter le nombre de journaux de vérification de statut
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} vérifications de statut")

    print("Adresses IP :")
    for ip in mongo_collection.aggregate(PIPE):
        print(f"\t{ip.get('_id')}: {ip.get('count')}")


if __name__ == "__main__":
    # Connexion à la collection MongoDB
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx

    # Analyse des statistiques des journaux
    log_stats(nginx_collection)
