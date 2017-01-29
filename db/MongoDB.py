from pymongo import MongoClient


class MongoDB:
    def __init__(self):
        self.db = None

    def openDB(self):
        connection = MongoClient('localhost', 27017)
        self.db = connection['bigearth']

    def insert(self, data):
        collection = self.db.countryfeatures
        result = collection.insert(data)
        print(result)
        # print(dataMongo)

        # def selectData(self):
    def clearTable(self):
        collection = self.db.countryfeatures
        collection.delete_many({})
