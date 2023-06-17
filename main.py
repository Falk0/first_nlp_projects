from text_processing.count_words import CountWords
from text_processing.n_grams import NGram


countedWords = CountWords('data/brown_corpus.txt')


countedWords.cleanText()
tokens = countedWords.tokenizeText()
countedWords.countWords()
countedWords.plotStatistic()

ngrams = NGram(tokens)
ngrams.generate_ngrams(3)
ngrams.count_ngrams()
ngrams.plotStatistic(5)
