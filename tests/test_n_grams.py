import unittest
import sys
import os


# Get the directory of the script being run:
current_directory = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (where your 'text_processing' module is) to the PYTHONPATH:
sys.path.append(os.path.join(current_directory, '..'))

from text_processing.n_grams import NGram


class TestNGrams(unittest.TestCase):
    
    def setUp(self):
        # Setup runs before each test case
        self.ngrams = NGram(['this', 'is', 'a', 'sentence'])

    def test_generate_and_count_ngrams(self):
        # Generate bigrams
        test1 = list(self.ngrams.generate_and_count_ngrams(2))
        print(test1)
        self.assertEqual([('this', 'is'),('is', 'a'),('a', 'sentence')], test1)
        test2 = list(self.ngrams.generate_and_count_ngrams(3))
        self.assertEqual([('this', 'is', 'a'),('is', 'a', 'sentence')], test2)




        
   
if __name__ == '__main__':
    unittest.main()
