from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        self.db = None
        self.collection = None
    def createInstance(self):
        connection = MongoClient('localhost', 27017)
        self.db = connection['bigearth']



    def insertData(self,dataMongo):
        collection = self.db.countryfeatures
        result = collection.insert_one(dataMongo)
        print(dataMongo)

    #def selectData(self):







