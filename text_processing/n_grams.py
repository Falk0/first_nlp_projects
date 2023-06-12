from collections import Counter


class NGram:
    # Create NGram object,
    def __init__(self, n, tokens):
        self.n = n
        self.tokens = None
        self.grams = None
        self.counted_bigrams = None

    def generate_ngrams(self):
        bigrams = zip(self.tokens, self.tokens[1:])
        return bigrams

    def count_ngrams(self):
        counted_bigrams = Counter(self.bigrams)
        print(self.counted_bigrams)


    