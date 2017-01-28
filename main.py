import pandas as pd
import math
import numpy as np

from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('fake.csv', index_col=0)
print (data)

y = np.array(data["f3"])
X = np.array(data.drop(["f3"], axis=1))
X = preprocessing.scale(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

print(X_train)
print(y_train)

reg = LinearRegression()
reg.fit (X_train, y_train)
print(reg.coef_)
accuracy = reg.score(X_test, y_test)
print(accuracy)
