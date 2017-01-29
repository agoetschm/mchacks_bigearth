# -*- coding: utf-8 -*-
from scraping.Scrapping import Scrapping
from db.MongoDB import MongoDB

class Main():
    if __name__=="__main__":

        scrappingObj = Scrapping()

        raw_data = scrappingObj.getScrappedData()
        # raw data in the form : {"country1":[f1, f2, ...], "country2": [f1, f2, ...], ...}
        # we want [{"country":country, "f1": f1, "f2": f2, ...}, {...}, ...]
        labels = raw_data["labels"]
        del raw_data["labels"]
        data = []
        for country, features in raw_data.items():
            features_dict = {}
            for label, feature in zip(labels, features):
                features_dict[label] = feature
            features_dict["country"] = country
            data += [features_dict]

        print(data)

        mongo = MongoDB()

        mongo.openDB()
        mongo.clearTable()
        mongo.insert(data)