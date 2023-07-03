#!/bin/bash

# Database name
database="my_db"

# Collection name
collection="school"

# Use the mongo command to delete all documents in the collection
mongo "$database" --quiet --eval "db.$collection.deleteMany({})" >/dev/null 2>&1
