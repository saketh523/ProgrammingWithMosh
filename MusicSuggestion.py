import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music_data = pd.read_csv('music.csv')
music_data
X = music_data.drop(columns = ['genre'])
y = music_data['genre']
model = DecisionTreeClassifier()
model.fit(X,y)
predictions = model.predict([[22,0]])
predictions