from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class Database:
    def __init__(self, uri='mongodb://host.docker.internal:27017', database_name='ProtoDEVDB'):
        self.uri = uri
        self.database_name = database_name
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.client.admin.command("ping")  # Verificar conexión
            self.db = self.client[self.database_name]
            print(f"Connected to MongoDB at {self.uri}, database: {self.database_name}")
        except ConnectionFailure as e:
            print(f"Connection failed: {e}")
            raise

    def get_collection(self, collection_name):
        if self.db is None:
            raise Exception("Database not connected. Call 'connect' first.")
        return self.db[collection_name]

    def close(self):
        if self.client:
            self.client.close()
            print("Connection to MongoDB closed.")
