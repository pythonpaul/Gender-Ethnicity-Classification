
import random
import ssl
import nltk
import ssl
import pandas as pd
import numpy as np
import sys

grocery_names = pd.read_csv('ethnicity_result.csv')
#print(grocery_names)
grocery_first = grocery_names['FIRST_NAME'].to_numpy()

#sys.exit()

# grocery_first = np.char.lower(grocery_first)
# lower case all items in array

print(len(grocery_first))

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# nltk.download('names')

from nltk.corpus import names


male_names = names.words('male.txt')
print(male_names)

sys.exit()

female_names = names.words('female.txt')
print(len(male_names))
print(len(female_names))

def gender_features(word):
    return {'last_letter': word[-1]}

labeled_names = ([(name, 'male') for name in names.words('male.txt')]+
[(name, 'female') for name in names.words('female.txt')])

random.shuffle(labeled_names)

# feature extractor
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]

train_set, test_set = featuresets[500:], featuresets[:500]

classifier = nltk.NaiveBayesClassifier.train(train_set)

#pass 

def classify():        
    count = 0
    for x in grocery_first:
        count+=1
        try:
            print(x, classifier.classify(gender_features(x)), nltk.classify.accuracy(classifier, train_set))
        except TypeError as t:
            print('not a string, pass')
            pass
        if count == 200:
            break
classify()
classifier.show_most_informative_features(10)


#print(classifier.classify(gender_features('savana')))
#print(classifier.classify(gender_feautres('savana')))
#print(nltk.classify.accuracy(classifier, train_set))


