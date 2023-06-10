import unittest
import sys
sys.path.append('/Users/falk/Documents/python_projects/first_nlp_projects')
from text_processing.count_words import CountWords

class TestCountWords(unittest.TestCase):
    
    def setUp(self):
        # Setup runs before each test case
        self.count_words = CountWords('data/test.txt')

    def test_cleanText(self):
        self.count_words.text = 'Hello, this is a text! 123'
        self.count_words.cleanText()
        self.assertEqual(self.count_words.text, 'hello this is a text ')

    def test_tokenizeText(self):
        self.count_words.text = 'hello this is a text'
        self.count_words.tokenizeText()
        self.assertEqual(self.count_words.tokens, ['hello', 'this', 'is', 'a', 'text'])

    def test_removeStopWords(self):
        self.count_words.tokens = ['hello', 'this', 'is', 'a', 'text']
        self.count_words.removeStopWords()
        self.assertEqual(self.count_words.tokens, ['hello', 'text'])

    def test_countWords(self):
        self.count_words.tokens = ['hello', 'text', 'example']
        numberOfWords = self.count_words.countWords()
        self.assertEqual(numberOfWords, 3)
        
   
if __name__ == '__main__':
    unittest.main()
