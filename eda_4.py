

import streamlit as st
import seaborn as sb
import pandas as pd 
import numpy as np 
from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import TimeSeriesSplit
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('train.csv')

data['month'] = data['time'].apply(lambda row: row.split('-')[1])
data['new_time'] = data['time'].apply(lambda row: row.split('-')[2][2:])
data['day'] = data['time'].apply(lambda row: row.split('-')[2][:2])

data = data.drop(['row_id', 'time'], axis=1)
# data = data[['x', 'y', 'direction', 'month', 'day', 'new_time', 'congestion']]

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

data['direction'] = label_encoder.fit_transform(data['direction'])



# data = data[['x', 'y', 'month', 'day', 'congestion']]
data



def pairing(data, seq_len=6):

    features = []
    target  = []

    for i in range(0, (data.shape[0] - seq_len+1), seq_len+1 ):   # range is reduced by the len of seq + 1 so that we do not go out of bounds
                                                                 # we step for that same amount of steps as the seq_len
        seq = np.zeros( (seq_len, data.shape[1]) )               # creating a matrix of zeros with the shape of seq_len and the number of columns of the data
         
        for j in range(seq_len):                                 # filling the matrix with the data

            seq[j] = data.values[i+j]                            # filling the matrix with the data we add i to make the jump of the seq_len

        features.append(seq.flatten())                                  # flattening the matrix and appending it to the x list
        target.append( data["congestion"][i+seq_len] )                  # appending the target to the y list 

    return np.array(features), np.array(target)

X, y = pairing(data)



time_series_clf = TimeSeriesSplit()
for train_index, test_index in time_series_clf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]


model_random = RandomForestRegressor()
model_random.fit(X_train, y_train)



model_random.score(X_test, y_test)


from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
# from sklearn.linear_model import SVR 

model_decision_tree = DecisionTreeClassifier()
model_decision_tree.fit(X_train, y_train)
model_decision_tree.score(X_test, y_test)
















