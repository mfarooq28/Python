from sklearn import tree
import fuzz as fuzzy()
#[height, weight, shoe size]
X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,70,40],[159,64,38],[171,75,42],[181,85,43]]
Y = ['male', 'female', 'female','female','male','male','male','female', 'male','female']
#clf = tree.DecisionTreeClassifier()
clf = fuzz.fuzzify()
clf = clf.fit(X,Y)

Prediction = clf.predict([[190,70,43]])

print(Prediction)
