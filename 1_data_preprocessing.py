# 1 Loading Data
import csv
# 1.1 Load all the app ids for each genre into a list
genres = ["education", "finance", "game", "social", "weather"]

app_id_list = []
for genre in genres:
	file_name = genre + ".csv"
	with open(file_name) as f: # omit newline='' for python 2
		reader = csv.reader(f)
		next(reader, None) 
		for row in reader:
			app_id = row[12]
			app_id_list.append((app_id, genre))

# 1.2 Load all the comments into the "data" object
# Tokenize, remove non ascii values, remove punctuation remove stop words before loading
# Use the default stop words but include "app"
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
stop_words = set(stop_words)
stop_words.add("app")

def remove_stop_words(word_tokens):
  filtered_sentence = [w for w in word_tokens if not w in stop_words]
  return filtered_sentence

def remove_non_ascii_1(text):
    return ''.join(i for i in text if ord(i)<128)


def remove_punctuation(text):
	return text.translate(string.maketrans("",""), string.punctuation)

data = []
counter = 0
for app in app_id_list:
	app_id = app[0]
	genre = app[1]
	file_name = app_id + ".csv"
	with open(file_name) as f: # omit newline='' for python 2
		reader = csv.reader(f)
		for row in reader:
			review = remove_punctuation(remove_non_ascii_1(row[4]).lower())
			review = word_tokenize(review)
			review = remove_stop_words(review)
			newlist = []
			for token in review:
				# Remove single character tokens
				if len(token) != 1:
					newlist.append(token)
			review = newlist
			# Skip reviews that are less than 5 tokens long after this preprocessing step
			if (len(review) <= 5):
				continue
			data.append((review, genre))
	counter += 1
	print counter

# Save data object with pickle for later use
import pickle
pickle.dump(data, open( "data.p", "wb" ) )



