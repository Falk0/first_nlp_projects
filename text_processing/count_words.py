## Simple class to load a text file, clean it, tokenize, remove "stop words", count the words
## and visualize results. 

import re 
import chardet
import nltk

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()
nltk.download('punkt')
nltk.download('brown')


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import matplotlib.pyplot as plt
from collections import Counter



class CountWords:
    # Create CountWords object, checking encoding if needed
    def __init__(self, path, encoding = False):
        self.path = path
        self.text = None
        self.tokens = None
        self.word_count = None
        
        if encoding:
            self.encoding = encoding
        else:
            try:
                with open(self.path, 'rb') as file:
                    self.encoding = chardet.detect(file.read())['encoding']
                    print(f'File encoded as: {self.encoding}')
            except Exception as e:
                print(f'Error reading the file: {e}')
        
        try:
            with open(self.path, 'r', encoding=self.encoding) as file:
                self.text = file.read()
        except Exception as e:
            print(f'Error reading the file: {e}')

    # remove ,.:!? and change to lower case. 
    def cleanText(self):
        self.text = re.sub('[^a-zA-Z\s]', '', self.text).lower()


    def tokenizeText(self):
        self.tokens = word_tokenize(self.text)
        return self.tokens
    

    # Remove stopwords like and, is, or 
    def removeStopWords(self, language = 'english'):
        if self.tokens != None:
            nltk.download('stopwords')
            stop_words = set(stopwords.words(language))
            self.tokens = [word for word in self.tokens if word not in stop_words]
        else:
            print('ERROR Text not tokenized')
            
        

    def countWords(self):
        self.word_count = Counter(self.tokens)
        return len(self.word_count)


    def lenText(self):
        print(len(self.text))


    def plotStatistic(self, number = 5):
        if self.word_count:
            top_words = self.word_count.most_common(number)
            plt.bar([word[0] for word in top_words], [word[1] for word in top_words])
            plt.xlabel('Words')
            plt.ylabel('Frequency')
            plt.title(f'Top {number} Words')
            plt.show()
        else: 
            print('ERROR words not counted')

