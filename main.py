import pandas as pd
import math
import numpy as np

from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score

data = pd.read_csv('fake1.csv', delimiter=';', index_col=0)
print (data.head())
print("-----------------------------------")

y = np.array(data["Lifeexpectancyatbirth"])
X = np.array(data.drop(["Lifeexpectancyatbirth"], axis=1))
X = preprocessing.scale(X)

reg = LinearRegression()#svm.SVR()

#scores = cross_val_score(reg, X, y, cv=3)
#print(scores)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

#print(X_train)
#print(y_train)
reg.fit (X_train, y_train)
#print(reg.coef_)

accuracy = reg.score(X_test, y_test)
print(accuracy)
