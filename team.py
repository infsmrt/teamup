# make predictions
from pandas import read_csv
from sklearn.svm import SVC
import numpy as np

def find(branch, position):
    # Load dataset
    dataset = read_csv("training.csv", header=0)

    # Split-out validation dataset
    array = dataset.values
    X = array[:,0:2]
    y = array[:,2]

    # Make predictions on validation dataset
    model = SVC(gamma='auto')
    model.fit(X, y)

    data = [[branch, position]]
    predictions = model.predict(data)
    return np.array2string(predictions)
