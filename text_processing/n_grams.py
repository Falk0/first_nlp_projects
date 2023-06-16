from collections import Counter


class NGram:
    # Create NGram object,
    def __init__(self, tokens):
        self.tokens = tokens
        self.grams = None
        self.counted_grams = None

    def generate_ngrams(self, n):
        ngrams = zip(*[self.tokens[i:] for i in range(n)])
        ngrams_list = [list(item) for item in ngrams]
        self.ngrams = list(ngrams_list)


    def count_ngrams(self):
        counted_grams = Counter(self.bigrams)
        print(self.counted_bigrams)


