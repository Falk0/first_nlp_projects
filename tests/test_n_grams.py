import unittest
import sys
sys.path.append('/Users/falk/Documents/python_projects/first_nlp_projects')
from text_processing.n_grams import NGram


class TestNGrams(unittest.TestCase):
    
    def setUp(self):
        # Setup runs before each test case
        self.ngrams = NGram()
        


    def test_generate_ngrams(self):
        bigrams = self.ngrams(2, ['this', 'is', 'a', 'sentence'])
        trigrams = self.ngrams(3, ['this', 'is', 'a', 'sentence'])
        
        self.assertEqual([['this', 'is'],['is', 'a'],['a', 'sentence']], bigrams)
        #self.assertEqual(self.count_words.text, 'hello this is a text ')
        pass

    def count_ngrams(self):
        pass
    

        
   
if __name__ == '__main__':
    unittest.main()
