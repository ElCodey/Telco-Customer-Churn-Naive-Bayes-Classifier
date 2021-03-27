import pandas as pd 
import numpy as np 
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import confusion_matrix

def cross_val_bayes(x, y):
    bayes = GaussianNB()
    cross_val = cross_val_score(bayes, x, y, cv=10)
    return cross_val.mean().round(2)

def bayes_model_conf_matrix(df, x, y):
    bayes = GaussianNB()
    X = df[x]
    Y = df[y]
    x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.8, random_state=42)
    fit_model = bayes.fit(x_train, y_train)
    y_pred = fit_model.predict(x_test)
    conf_matrix = confusion_matrix(y_test, y_pred)
    return conf_matrix
