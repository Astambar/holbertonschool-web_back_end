#!/usr/bin/env python3
""" 11-schools_by_topic.py """


def schools_by_topic(mongo_collection, topic):
    """ 11-schools_by_topic.py """
    return mongo_collection.find({"topics": topic})
