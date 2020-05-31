import numpy as np 
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
 
df = pd.read_csv("https://sebkaz.github.io/teaching/PrzetwarzanieDanych/data/polish_names.csv")

def target(string): return int(string == 'm')
def is_last_a(string): return int(string[-1] == 'a')

def getAccuracyScore():

    df['target'] = df['gender'].map(target)
    df['is_last_a'] = df['name'].map(is_last_a)

    y = df['target'].values
    x = df[['is_last_a']].values

    model = LogisticRegression()
    model.fit(x, y)

    y_pred = model.predict(x)
    return accuracy_score(y, y_pred)
