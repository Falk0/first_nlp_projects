import unittest
from count_words import CountWords

class TestCountWords(unittest.TestCase):
    
    def setUp(self):
        # Setup runs before each test case
        self.count_words = CountWords('path_to_test_file.txt')
        
    def test_clean_text(self):
        self.count_words.text = "Hello, World! 123."
        self.count_words.clean_text()
        self.assertEqual(self.count_words.text, "hello world")
        
    def test_tokenize_text(self):
        self.count_words.text = "hello world"
        self.count_words.tokenize_text()
        self.assertEqual(self.count_words.tokens, ['hello', 'world'])

    def test_count_words(self):
        self.count_words.tokens = ['hello', 'world', 'hello']
        self.count_words.count_words()
        self.assertEqual(self.count_words.word_count, {'hello': 2, 'world': 1})

    def test_remove_stop_words(self):
        self.count_words.tokens = ['this', 'is', 'a', 'test']
        self.count_words.remove_stop_words()
        self.assertEqual(self.count_words.tokens, ['test'])

if __name__ == '__main__':
    unittest.main()
