from pymongo import MongoClient
import pymongo


class MongoDB:
    def __init__(self, database_name, uri):
        self.client = MongoClient(uri)
        self.database = self.client[database_name]

    def database_config(self):
        return self.database

    @staticmethod
    def find_dictionary(programming, query):
        return programming.find(query)

    def find_one(self, collection: str, query: dict):
        return self.database[collection].find_one(query, {'_id': False})

    def find_one_lasted(self, collection: str, query: dict):
        return self.database[collection].find_one(query, sort=[('_id', pymongo.DESCENDING)])

    def find(self, collection: str, query: dict):
        return self.database[collection].find(query, {'_id': False})

    def insert_one(self, collection: str, data: dict):
        ids = None
        try:
            result = self.database[collection].insert_one(data)
            ids = result.inserted_ids
        except Exception as e:
            print(str(e))
        return ids

    def insert_many(self, collection: str, data: list):
        ids = None
        try:
            result = self.database[collection].insert_many(data)
            ids = result.inserted_ids
        except Exception as e:
            print(str(e))
        return ids

    def update_many(self, collection: str, query: dict, values):
        try:
            self.database[collection].update_many(query, values)
        except Exception as e:
            print(str(e))

    def update_one(self, collection: str, query: dict, values):
        try:
            self.database[collection].update_one(query, values)
        except Exception as e:
            print(str(e))

    def delete_one(self, collection: str, query: dict):
        try:
            self.database[collection].delete_one(query)
        except Exception as e:
            print(str(e))

    def delete_many(self, collection: str, query: dict):
        try:
            self.database[collection].delete_many(query)
        except Exception as e:
            print(str(e))
