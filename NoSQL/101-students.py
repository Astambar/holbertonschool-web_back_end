#!/usr/bin/env python3
""" 101-students.py """


def top_students(mongo_collection):
    """ Récupère les meilleurs étudiants à partir d'une collection MongoDB """
    pipeline = [
        {
            '$project': {
                'name': 1,
                'averageScore': { '$avg': '$topics.score' }
            }
        },
        { '$sort': { 'averageScore': -1 } }
    ]
    return list(mongo_collection.aggregate(pipeline))
