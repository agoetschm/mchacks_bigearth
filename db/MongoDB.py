from pymongo import MongoClient
import pandas as pd

from db.DataFormatter import DataFormatter


class MongoDB:
    def __init__(self):
        self.connection = None
        self.db = None

    def openDB(self):
        self.connection = MongoClient('localhost', 27017)
        self.db = self.connection['bigearth']

    def close(self):
        self.connection.close()

    def insert(self, data):
        collection = self.db.countryfeatures
        result = collection.insert(DataFormatter().format(data))
        #print(result)

    def clearTable(self):
        collection = self.db.countryfeatures
        collection.delete_many({})

    def getDataFrame(self):
        collection = self.db.countryfeatures
        df = pd.DataFrame(list(collection.find()))
        df = df.drop("_id", axis=1)
        df = df.set_index("country")
        return df
