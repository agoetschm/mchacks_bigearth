import pandas as pd
import math
import numpy as np

from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression

data = pd.read_csv('fake.csv', index_col=0)
print (data)
y = np.array(data["f3"])
X = np.array(data.drop(["f3"], axis=1))

reg = LinearRegression()
reg.fit (X, y)
print(reg.coef_)
