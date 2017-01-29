# -*- coding: utf-8 -*-
import math

from regression.Regression import Regression
from scraping.Scraping import Scraping
from db.MongoDB import MongoDB
import numpy as np
import matplotlib.pyplot as plt


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
        coefs = Regression().execute(df)

        vs = []
        ls = []
        for l, v in coefs:
            vs += [math.fabs(v)]
            ls += [l]
        x_pos = np.arange(len(coefs))
        plt.barh(x_pos, vs)
        plt.yticks(x_pos, ls)
        plt.title("(Maybe) influence of features on\nthe happiness rate in a country")
        plt.tight_layout(pad=0)
        #plt.axis([0, len(c), -10, 10])
        #plt.show()
        plt.savefig("figure1")

        mongo.close()
