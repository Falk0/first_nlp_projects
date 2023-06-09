## Simple class to load a text file, clean it, tokenize, remove "stop words", count the words
## and visualize results. 

import re 
import pandas 
import chardet
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import matplotlib.pyplot as plt

class CountWords:
    # Create CountWords object, checking encoding if needed
    def __init__(self, path, encoding = False):
        self.path = path
        self.text = None
        self.tokens = None
        
        if encoding:
            self.encoding = encoding
        else:
            with open(self.path, 'rb') as file:
                self.encoding = chardet.detect(file.read())['encoding']
                print(f'File encoded as: {self.encoding}')
    
        with open(self.path, 'r', encoding=self.encoding) as file:
            self.text = file.read()


    # remove ,.:!? and change to lower case. 
    def cleanText(self):
        self.text = re.sub('[^a-zA-Z\s]', '', self.text).lower()


    def tokenizeText(self):
        self.tokens = word_tokenize(self.text)
    
    # Remove stopwords like and, is, or 
    def removeStopWords(self, language = 'english'):
        if self.tokens != None:
            nltk.download('stopwords')
            stop_words = set(stopwords.words(language))
            self.tokens = [word for word in self.tokens if word not in stop_words]
        else:
            print('ERROR Text not tokenized')
            
        

    def count(self):
        pass


    def lenText(self):
        print(len(self.text))

    def plotStatistic(number = 5):
        pass





countedWords = CountWords('data/lorem.txt')


countedWords.lenText()
countedWords.cleanText()
countedWords.lenText()
countedWords.tokenizeText()
print(len(countedWords.tokens))
countedWords.removeStopWords()
print(len(countedWords.tokens))