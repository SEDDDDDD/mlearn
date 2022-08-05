import numpy as np
import pandas as pd
from sklearn import datasets
#
from sklearn import model_selection
from sklearn.svm import SVC
from sklearn import metrics

dataset = datasets.load_wine()



x_data = dataset.data
y_data = dataset.target


####################

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_data)
x_data = scaler.transform(x_data)

x_train, x_test, y_train, y_test = model_selection.train_test_split(x_data, y_data, test_size=0.33)

estimator = SVC(kernel='rbf', C=1.0, gamma='auto')

estimator.fit(x_train, y_train)

y_predict = estimator.predict(x_train)
score = metrics.accuracy_score(y_train, y_predict)
print(score) #1.0

y_predict = estimator.predict(x_test)
score = metrics.accuracy_score(y_test, y_predict)
print(score) #1.0