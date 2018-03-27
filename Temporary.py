
print ("Number of entries: ", len(train_feats))
for featurename in wine.feature_names:
    print (featurename[:10], "    \t")
print ("Class")
for feature, label in zip(train_feats, test_labels):
    for f in feature:
        print (f, "\t\t")
    print (label)
