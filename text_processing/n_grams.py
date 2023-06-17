from collections import Counter
import matplotlib.pyplot as plt


class NGram:
    # Create NGram object,
    def __init__(self, tokens):
        self.tokens = tokens
        self.grams = None
        self.counted_grams = None

    def generate_ngrams(self, n):
        ngrams = zip(*[self.tokens[i:] for i in range(n)])
        ngrams_list = list(ngrams)
        self.grams = ngrams_list
        return self.grams

    def count_ngrams(self):
        self.counted_grams = Counter(self.grams)
        return self.counted_grams

    def plotStatistic(self, number = 5):
        if self.counted_grams:
            grams = self.count_ngrams()
            top_grams = grams.most_common(number)
            gram_labels = [str(gram) for gram, count in top_grams]
            gram_counts = [count for gram, count in top_grams]
            
            plt.bar(gram_labels, gram_counts)
            plt.xticks(rotation=90, ha='right')
            plt.xlabel('Grams')
            plt.ylabel('Frequency')
            plt.title(f'Top {number} grams')
            plt.show()
        else: 
            print('ERROR words not counted')

