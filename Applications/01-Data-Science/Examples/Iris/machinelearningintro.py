# Learning Resource
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# https://machinelearningmastery.com/k-fold-cross-validation/
# https://machinelearningmastery.com/make-predictions-scikit-learn/
# https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/

# Load libraries
from pandas 						import read_csv
from pandas.plotting 				import scatter_matrix
from matplotlib 					import pyplot
from sklearn.model_selection 		import train_test_split
from sklearn.model_selection 		import cross_val_score
from sklearn.model_selection 		import StratifiedKFold
from sklearn.metrics 				import classification_report
from sklearn.metrics 				import confusion_matrix
from sklearn.metrics 				import accuracy_score
from sklearn.linear_model 			import LogisticRegression
from sklearn.tree 					import DecisionTreeClassifier
from sklearn.neighbors 				import KNeighborsClassifier
from sklearn.discriminant_analysis 	import LinearDiscriminantAnalysis
from sklearn.naive_bayes 			import GaussianNB
from sklearn.svm 					import SVC

# Load dataset
url = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# --- Summarize Dataset ---

print("\n-------------------")
print("    Dimensions")
print("-------------------\n")

# dimensions of dataset
print(dataset.shape)

print("\n-------------------")
print("    View Data")
print("-------------------\n")

# view data
print(dataset.head(20))

print("\n-------------------")
print("  Summarize Data")
print("-------------------\n")

# summarize data
print(dataset.describe())

print("\n----------------------")
print("  Class Distribution")
print("----------------------\n")

# class distribution
print(dataset.groupby('class').size())

# --- Data Visualization ---

# # box and whisker plots
# dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# pyplot.show()

# # histograms
# dataset.hist()
# pyplot.show()

# # scatter plot matrix
# scatter_matrix(dataset)
# pyplot.show()

# --- Data Validation ---

# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

# Six Different Algorithms
# 1 ... Logistic Regression (LR)
# 2 ... Linear Discriminant Analysis (LDA)
# 3 ... K-Nearest Neighbors (KNN)
# 4 ... Classification and Regression Trees (CART)
# 5 ... Gaussian Naive Bayes (NB)
# 6 ... Support Vector Machines (SVM)

print("\n-------------------")
print("   Build Models")
print("-------------------\n")

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))


# # Compare Algorithms
# pyplot.boxplot(results, labels=names)
# pyplot.title('Algorithm Comparison')
# pyplot.show()

# --- Make Predictions ---

# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

print("\n------------------------")
print("  Evaluate Predictions")
print("------------------------\n")

# Evaluate predictions
print("{:.3f}%".format(accuracy_score(Y_validation, predictions)))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))















