import unittest
import sys
sys.path.append('/Users/falk/Documents/python_projects/first_nlp_projects')
from text_processing.n_grams import NGram


class TestNGrams(unittest.TestCase):
    
    def setUp(self):
        # Setup runs before each test case
        self.ngrams = NGram(['this', 'is', 'a', 'sentence'])
        


    def test_generate_ngrams(self):
        # Generate bigrams
        self.ngrams.generate_ngrams(2)
        self.assertEqual([['this', 'is'],['is', 'a'],['a', 'sentence']], self.ngrams.ngrams)
        self.ngrams.generate_ngrams(3)
        self.assertEqual([['this', 'is', 'a'],['is', 'a', 'sentence']], self.ngrams.ngrams)

    def count_ngrams(self):
        pass
    

        
   
if __name__ == '__main__':
    unittest.main()
