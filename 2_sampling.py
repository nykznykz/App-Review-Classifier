import cPickle as pickle

data = pickle.load(open("data.p", "rb"))

genres = ["education", "finance", "game", "social", "weather"]

import random
#Understanding Distribution
for genre in genres:
	counter = 0
	for rev in data:
		if rev[1] == genre:
			counter += 1
	print genre + " " + str(counter)

# Observe that it's best to sample 50,000 from each genre to ensure equal data.
random.shuffle(data)

quotas = {"education": 0, "finance": 0, "game": 0, "social": 0, "weather": 0}

sample = []
test_data = []
words = []
for rev in data:
	if quotas[rev[1]] < 10000:
		sample.append(rev)
		words += rev[0]
		quotas[rev[1]] = quotas[rev[1]] + 1
	elif quotas[rev[1]] < 12000:
		test_data.append(rev)
		quotas[rev[1]] = quotas[rev[1]] + 1
	counter += 1

print words[:100]
print len(sample)
print len(test_data)

random.shuffle(sample)
pickle.dump(sample, open( "data_sample.p", "wb" ) )
pickle.dump(test_data, open( "test_data.p", "wb" ) )
pickle.dump(words, open( "data_sample_words.p", "wb" ) )