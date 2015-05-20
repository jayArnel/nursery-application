from methods import *
from sklearn import svm

# print "Retrieving and partitioning dataset"
dataset = get_dataset('nursery.dat')
dataset, encoders = encode(dataset)
X_train, Y_train, X_test, Y_test = partition(dataset)

# print "Training SVM"
# gammaSteps = [0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1]
# CSteps = [1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000];
# maxScore = 0
# optC = 0
# optGamma = 0
# for tempC in CSteps:
#     for tempGamma in gammaSteps:
#         clf = svm.SVC(C=tempC, gamma=tempGamma)
#         clf.fit(X_train, Y_train)
#         score = clf.score(X_test, Y_test)
#         print "C: {0}, gamma: {1}, score: {2}".format(tempC, tempGamma, score)
#         if score > maxScore:
#             optC = tempC
#             optGamma = tempGamma
#             maxScore = score
# print "optimum:\n C: {0}, gamma: {1}, score: {2}".format(optC, optGamma, maxScore)
optC = 300
optGamma = 0.1
def predict(X):
    clf = svm.SVC(C=optC, gamma=optGamma)
    X = encoders[i].transform(X)
    X = preprocessing.scale(X)
    print clf.predict(X)
