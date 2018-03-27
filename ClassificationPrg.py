from __future__ import division, print_function
from sklearn import datasets
from sklearn import svm
from sklearn import tree

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split as tts
wine = datasets.load_wine()

features = wine.data
labels = wine.target

train_feats, test_feats, train_labels, test_labels = tts(features, labels, test_size =0.2)

#clf=tree.DecisionTreeClassifier()
#clf = RandomForestClassifier()
clf =svm.SVC()

clf.fit(train_feats,train_labels)

Predictions = clf.predict(test_feats)

print(Predictions)

print()

score = 0
for i in range(len(Predictions)):
    if Predictions[i] == test_labels[i]:
        score += 1
print(score/len(Predictions))
