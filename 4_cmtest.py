# Analysis of errors using a confusion matrix
import nltk
from nltk.metrics import ConfusionMatrix
import cPickle as pickle

all_words = pickle.load(open("data_sample_words.p", "rb"))
all_words = nltk.FreqDist(all_words)
word_features = sorted(all_words, key=all_words.get, reverse=True)[:5000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

train_data = pickle.load(open("data_sample.p", "rb"))
test_data = pickle.load(open("test_data.p", "rb"))
print "loaded"
actual_values = [category for (rev, category) in test_data]
testing_set = [find_features(rev) for (rev, category) in test_data]
print "constucted feature sets"

# actual_values = []
# for row in test_data:
# 	actual_values.append(row[1])

# print actual_values[:10]

classifier = pickle.load(open("ONBClassifier.p", "rb"))
pred_values =[]
for feature_set in testing_set:
	pred_value = classifier.classify(feature_set)
	pred_values.append(pred_value)


cm = nltk.ConfusionMatrix(actual_values, pred_values)
print(cm.pretty_format(sort_by_count=True, show_percents=True, truncate=9))
