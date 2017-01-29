# -*- coding: utf-8 -*-
from Scrapping import Scrapping
from MongoDB import MongoDB

class Main():
    if __name__=="__main__":

        scrappingObj = Scrapping()

        data = scrappingObj.getScrappedData()
        #data=  {"author": "Mike",  "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"]}

        mongo = MongoDB()

        mongo.createInstance()
        mongo.insertData(data)