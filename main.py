from text_processing.count_words import CountWords
from text_processing.n_grams import NGram


countedWords = CountWords('data/brown_corpus.txt')


countedWords.cleanText()
tokens = countedWords.tokenizeText()
#countedWords.removeStopWords()
countedWords.countWords()
countedWords.plotStatistic()

ngrams = NGram(tokens)
ngrams.generate_and_count_ngrams(3)
ngrams.get_specific_ngram(('as', 'well', 'as'))
ngrams.plotStatistic()

