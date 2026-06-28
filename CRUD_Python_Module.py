from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for the AAC animal collection in MongoDB."""

    def __init__(self, user="aacuser", password="SNHU1234"):
        USER = user
        PASS = password
        HOST = "localhost"
        PORT = 27017
        DB = "aac"
        COL = "animals"

        self.client = MongoClient(f"mongodb://{USER}:{PASS}@{HOST}:{PORT}")
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Insert a document into the animals collection."""
        if data is not None and isinstance(data, dict):
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Insert error:", e)
                return False

        return False

    def read(self, query):
        """Read documents from the animals collection using find()."""
        if query is not None and isinstance(query, dict):
            try:
                results = self.collection.find(query)
                return list(results)
            except Exception as e:
                print("Read error:", e)
                return []

        return []

    def update(self, query, new_values):
        """Update document(s) in the animals collection."""
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(
                    query,
                    {"$set": new_values}
                )
                return result.modified_count
            except Exception as e:
                print("Update error:", e)
                return 0

        return 0

    def delete(self, query):
        """Delete document(s) from the animals collection."""
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Delete error:", e)
                return 0

        return 0