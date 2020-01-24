# make predictions
from pandas import read_csv
from sklearn.svm import SVC
import numpy as np

def find(branch, position):
    # Load dataset
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = read_csv(url, names=names)

    # Split-out validation dataset
    array = dataset.values
    X = array[:,0:4]
    y = array[:,4]

    # Make predictions on validation dataset
    model = SVC(gamma='auto')
    model.fit(X, y)

    data = [[6.8, 4.0, 1.2, 2]]
    predictions = model.predict(data)
    return np.array2string(predictions)
