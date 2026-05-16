import numpy
from scipy import stats
import matplotlib.pyplot as plt
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

def basics():
    data = [86,87,88,86,87,85,86,32,111,138,28,59,77,97]

    print('Mean:', numpy.mean(data))
    print('Median:', numpy.median(data))
    print('Mode:', stats.mode(data).mode, 'occurred', stats.mode(data).count, 'times')
    print('Min:', numpy.min(data))
    print('Max:', numpy.max(data))
    print('Standard Deviation:', numpy.std(data))
    print('Percentile 70:', numpy.percentile(data, 70))
    print('Percentile 90:', numpy.percentile(data, 90))
    print('Percentile 99:', numpy.percentile(data, 99))


def uniform_data():
    """ create a random, uniform dataset """
    uniform_data = numpy.random.uniform(0.0, 20.0, 50)
    print(uniform_data)
    plt.hist(uniform_data, 5)
    plt.show()


def normal_data():
    """ create a random, normal dataset """
    normal_data = numpy.random.normal(5.0, 1.0, 100000)
    print(normal_data)
    plt.hist(normal_data, 100)
    plt.show()


def linear_regression():
    """ Fit the dataset with a linear line """
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
      return slope * x + intercept

    mymodel = list(map(myfunc, x))

    print('R:', r)
    print('Predicition (10):', myfunc(10))

    plt.scatter(x, y)
    plt.plot(x, mymodel)
    plt.show()


def polynomial_regression():
    """ Fit the dataset with a polynomial curve """
    x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
    y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

    mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

    myline = numpy.linspace(1, 22, 100)

    print('R-Squared:', r2_score(y, mymodel(x)))
    print('Prediction (17):', mymodel(17))

    plt.scatter(x, y)
    plt.plot(myline, mymodel(myline))
    plt.show()


def multiple_regression():
    """ Linear regression with multiple independent variables """
    df = pandas.read_csv("cars.csv")

    X = df[['Weight', 'Volume']]
    y = df['CO2']

    regr = linear_model.LinearRegression()
    regr.fit(X, y)

    print('Regression Coefficient:', regr.coef_)

    #predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
    predictedCO2 = regr.predict([[2300, 1300]])
    print('Predicted (2300, 1300):', predictedCO2)


def scale_data():
    """ Scale data to perform analysis on the scaled values """
    scale = StandardScaler()

    df = pandas.read_csv("cars2.csv")

    X = df[['Weight', 'Volume']]
    y = df['CO2']

    scaledX = scale.fit_transform(X)

    print(scaledX)

    regr = linear_model.LinearRegression()
    regr.fit(scaledX, y)

    scaled = scale.transform([[2300, 1.3]])

    predictedCO2 = regr.predict([scaled[0]])
    print(predictedCO2)


if __name__ == '__main__':
    basics()
    #uniform_data()
    #normal_data()
    #linear_regression()
    #polynomial_regression()
    #multiple_regression()
    #scale_data()