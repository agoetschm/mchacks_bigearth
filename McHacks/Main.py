# -*- coding: utf-8 -*-
from Scrapping import Scrapping
from MongoDB import MongoDB

class Main():
    if __name__=="__main__":

        scrappingObj = Scrapping()

        raw_data = scrappingObj.getScrappedData()
        # data in the form : {"country1":[f1, f2, ...], "country2": [f1, f2, ...], ...}
        # we want {"country1":{"f1": f1, "f2": f2, ...}, "country2": ...}
        labels = raw_data["labels"]
        del raw_data["labels"]
        data = {}
        for country, features in raw_data.items():
            features_dict = {}
            # print(features)
            for label, feature in zip(labels, features):
                features_dict[label] = feature
            features_dict["country"] = country
            data[country] = features_dict

        print(data)

        #data=  {"author": "Mike",  "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"]}

        mongo = MongoDB()

        mongo.createInstance()
        mongo.insertData(data)