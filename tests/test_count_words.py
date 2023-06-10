import unittest
from text_processing.count_words import CountWords

class TestCountWords(unittest.TestCase):
    
    def setUp(self):
        # Setup runs before each test case
        self.count_words = CountWords('path_to_test_file.txt')
        
   
if __name__ == '__main__':
    unittest.main()
