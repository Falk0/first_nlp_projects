## Simple script to load a text file, clean it, tokenize, remove "stop words", count the words
## and finaly visualize the result. 

import re 
import pandas 
import chardet


# First check what encoding the text file as
with open('data/lorem.txt', 'rb') as file:
    result = chardet.detect(file.read())


encoding = result['encoding']

print(encoding)
