## Written By Farooq

# Add Preprocessed Libraries
from sklearn import tree
from sklearn import svm
from sklearn import neighbors

# [Height, Weight, Shoe Size]
X = [[181,80,44], [177,70,43], [160,60,38], [154, 54, 37], [166,65,40],
     [190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42],[181,85,43]]
Y= ['male', 'male','female','female','male','male','female','female',
    'female', 'male', 'male']

clf = tree.DecisionTreeClassifier()
clf_svm=svm.SVC()
clf_knn=neighbors.KNeighborsClassifier()

# Evaluate Fitness
clf_tree =clf.fit(X,Y)
clf_svm=clf.fit(X,Y)
clf_knn=clf.fit(X,Y)

# Predicition Step
predicitTree = clf_tree.predict([[155,54,36]])
predicitSVM=clf_svm.predict([[179,74,44]])
predicitKNN=clf_knn.predict([[141,110,36]])

# Printing
print(predicitTree)
print()
print(predicitSVM)
print()
print(predicitKNN)
