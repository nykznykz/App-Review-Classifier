# Selection of features, training and testing of Naive Bayes Classifier
import cPickle as pickle

import nltk
from nltk.classify.scikitlearn import SklearnClassifier

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

# from nltk.classify import ClassifierI
# from statistics import mode

# Choosing the 5000 most common words to be features
all_words = pickle.load(open("data_sample_words.p", "rb"))
all_words = nltk.FreqDist(all_words)
word_features = sorted(all_words, key=all_words.get, reverse=True)[:5000]

# class VoteClassifier(ClassifierI):
#     def __init__(self, *classifiers):
#         self._classifiers = classifiers

#     def classify(self, features):
#         votes = []
#         for c in self._classifiers:
#             v = c.classify(features)
#             votes.append(v)
#             print votes
#         return mode(votes)

#     def confidence(self, features):
#         votes = []
#         for c in self._classifiers:
#             v = c.classify(features)
#             votes.append(v)

#         choice_votes = votes.count(mode(votes))
#         conf = choice_votes / len(votes)
#         return conf


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

train_data = pickle.load(open("data_sample.p", "rb"))
test_data = pickle.load(open("test_data.p", "rb"))
print "loaded"
training_set = [(find_features(rev), category) for (rev, category) in train_data]
testing_set = [(find_features(rev), category) for (rev, category) in test_data]
print "constucted feature sets"

ONBclassifier = nltk.NaiveBayesClassifier.train(training_set)
print "classifier trained"
pickle.dump(ONBclassifier, open("ONBclassifier.p", "wb"))
print "dumped"
print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(ONBclassifier, testing_set))*100)
ONBclassifier.show_most_informative_features(15)


# MNB_classifier = SklearnClassifier(MultinomialNB())
# MNB_classifier.train(training_set)
# pickle.dump(MNB_classifier, open("MNB_classifier.p", "wb"))
# print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)


# BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
# BernoulliNB_classifier.train(training_set)
# print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

# LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
# LogisticRegression_classifier.train(training_set)
# print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

# SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
# SGDClassifier_classifier.train(training_set)
# print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

#SVC_classifier = SklearnClassifier(SVC())
#SVC_classifier.train(training_set)
#print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

# LinearSVC_classifier = SklearnClassifier(LinearSVC())
# LinearSVC_classifier.train(training_set)
# print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

# NuSVC_classifier = SklearnClassifier(NuSVC())
# NuSVC_classifier.train(training_set)
# print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)


# voted_classifier = VoteClassifier(ONBclassifier,
#                                   SGDClassifier_classifier,
#                                   MNB_classifier,
#                                   BernoulliNB_classifier,
#                                   LogisticRegression_classifier)
#Save classifiers

# pickle.dump(MNB_classifier, open( "MNB_classifier.p", "wb" ) )
# pickle.dump(BernoulliNB_classifier, open( "BernoulliNB_classifier.p", "wb" ) )
# pickle.dump(LogisticRegression_classifier, open( "LogisticRegression_classifier.p", "wb" ) )
# pickle.dump(SGDClassifier_classifier, open( "SGDClassifier_classifier.p", "wb" ) )
# pickle.dump(LinearSVC_classifier, open( "LinearSVC_classifier.p", "wb" ) )
# pickle.dump(MNuSVC_classifier, open( "NuSVC_classifier.p", "wb" ) )

# print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)

# print("Classification:", voted_classifier.classify(testing_set[0][0]), "Confidence %:",voted_classifier.confidence(testing_set[0][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[1][0]), "Confidence %:",voted_classifier.confidence(testing_set[1][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[2][0]), "Confidence %:",voted_classifier.confidence(testing_set[2][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[3][0]), "Confidence %:",voted_classifier.confidence(testing_set[3][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[4][0]), "Confidence %:",voted_classifier.confidence(testing_set[4][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[5][0]), "Confidence %:",voted_classifier.confidence(testing_set[5][0])*100)