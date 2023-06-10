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
        pass

    def test_removeStopWords(self):
        pass

    def test_countWords(self):
        pass
        
   
if __name__ == '__main__':
    unittest.main()
