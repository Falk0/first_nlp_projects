from collections import Counter
import matplotlib.pyplot as plt


class NGram:
    # Create NGram object,
    def __init__(self, tokens):
        if type(tokens) == list: 
            self.tokens = tokens
            self.counted_grams = None
        else:
            print('Tokens must be a list')
        
    # Generate n-grams 
    def generate_and_count_ngrams(self, n):
        ngrams = zip(*[self.tokens[i:] for i in range(n)])
        self.counted_grams = Counter(ngrams)
        return self.counted_grams
    
    
    def get_specific_ngram(self, ngram):
        return self.counted_grams.get(ngram, 0)
        

    def plotStatistic(self, number = 5):
        if self.counted_grams:
            top_grams = self.counted_grams.most_common(number)
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

