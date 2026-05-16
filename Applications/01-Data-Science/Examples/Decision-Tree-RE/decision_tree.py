import os
import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_percentage_error
import joblib

from sklearn import tree
import pydotplus
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

data_file = 'redata'
saved_model_file = data_file + '.joblib'

if os.path.isfile(saved_model_file):
    # re-load previously saved model
    model = joblib.load(saved_model_file)
    prediction = model.predict([[180,3675,5,5,2005,2005,0,0,547,1072,0,2,1,5,0,2,525]])
    print(prediction)
else:
    music_data = pandas.read_csv(data_file + '.csv')
    X = music_data.drop(columns=['SalePrice'])
    y = music_data['SalePrice']

    # split data into testing and training data
    X_train, X_test, y_train, y_test = train_test_split(X.values, y, test_size=0.25)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # save model for future use
    joblib.dump(model, saved_model_file)

    # graph decision tree
    data = tree.export_graphviz(model, out_file=None, feature_names=X.columns, 
                                label='all', rounded=True, filled=True)
    graph = pydotplus.graph_from_dot_data(data)
    graph.write_png('mydecisiontree.png')
    img = pltimg.imread('mydecisiontree.png')
    imgplot = plt.imshow(img)

    # calculate accuracy of model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    mape = mean_absolute_percentage_error(y_test, predictions)
    print('Accuracy:', accuracy)
    print('R-Squared:', r2)
    print('MAPE:', mape)