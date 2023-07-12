from text_processing.count_words import CountWords
from text_processing.n_grams import NGram
from text_processing.markovchain_generator import Markovchain_generator

countedWords = CountWords('data/brown_corpus.txt')


countedWords.cleanText()
tokens = countedWords.tokenizeText()
#countedWords.removeStopWords()
countedWords.countWords()
#countedWords.plotStatistic()

ngrams = NGram(tokens)
#gramm = ngrams.generate_and_count_ngrams(3)
#test = ngrams.get_specific_ngram(('as', 'well', 'as'))
#ngrams.plotStatistic()

markov = Markovchain_generator(tokens)
dict = markov.build_probability_dict()
sent = markov.generate_sentence(10, 'my')
print(sent)