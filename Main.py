# -*- coding: utf-8 -*-
from regression.Regression import Regression
from scraping.Scraping import Scraping
from db.MongoDB import MongoDB


class Main():


    if __name__ == "__main__":

        # scrappingObj = Scrapping()
        #
        # raw_data = scrappingObj.getScrappedData()

        mongo = MongoDB()

        mongo.openDB()
        # mongo.clearTable()
        # mongo.insert(raw_data)

        df = mongo.getDataFrame()
        print(df.head())
        Regression().execute(df)

        mongo.close()
