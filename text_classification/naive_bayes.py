

from sklearn.feature_extraction.text import CountVectorizer
categories = ['comp.graphics'] #['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']
from sklearn.datasets import fetch_20newsgroups
train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)

print(train.target_names)

count_vector = CountVectorizer()

#Bags of word vectorizing 
train_counts = count_vector.fit_transform(train.data)

bigram = count_vector.vocabulary_.get(u'algorithm')

print(bigram)