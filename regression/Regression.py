import pandas as pd
import math
import numpy as np
import scipy

from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score


class Regression:
    def execute(self, df):
        # df.fillna(0, inplace=True)

        # df=df[["EmploymentRate", "HappinessRate"]]


        y = np.nan_to_num(np.array(df["HappinessRate"]))
        X = np.nan_to_num(np.array(df.drop(["HappinessRate"], axis=1)))
        X = preprocessing.scale(X)
        print(X)

        # reg = LinearRegression()  #
        reg = svm.SVR(kernel='linear')

        # scores = cross_val_score(reg, X, y, cv=5)
        # print(scores)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        print("Training set size : " + str(len(X_train)))
        print("Testing set size : " + str(len(X_test)))

        # print(X_train)
        # print(y_train)
        reg.fit(X_train, y_train)

        coefs = reg.coef_

        accuracy = reg.score(X_test, y_test)
        print(accuracy)

        labels = list(df)
        labels.remove("HappinessRate")

        coefForFeature = list(zip(labels, coefs[0]))
        return coefForFeature
