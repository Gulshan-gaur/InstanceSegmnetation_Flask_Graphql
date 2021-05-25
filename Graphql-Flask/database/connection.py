from pymongo import MongoClient

class Database(object):
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")  # configure db url
        self.db = self.client.API
        print("🚀"+"mongodb is running") 
        

