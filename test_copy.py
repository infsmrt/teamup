# make predictions
import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

# Load dataset
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
# names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# dataset = read_csv(url, names=names)
#
# # Split-out validation dataset
# array = dataset.values
# X = array[:,0:4]
# y = array[:,4]

fileName = "C:/Users/user-infsmrt/Downloads/team.data"
#dataset = read_excel(fileName, sheet_name="Final", header=0, na_values="")
dataset = read_csv("C:/Users/user-infsmrt/Downloads/team.data")
dataset.describe()

# Split-out validation dataset
array = dataset.values

X = array[:,0:2]
y = array[:,2]

#X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, y_train)

#print(X_validation)
#predictions = model.predict(X_validation)

y_pred = model.predict(X_test)
df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
df


# data = [[358,1], [622,2]]
# predictions = model.predict(data)
# print(predictions)

# Evaluate predictions
#print(accuracy_score(Y_validation, predictions))
#print(confusion_matrix(Y_validation, predictions))
#print(classification_report(Y_validation, predictions))