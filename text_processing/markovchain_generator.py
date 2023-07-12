from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import random
import numpy as np

class Markovchain_generator:
    # Create NGram object,
    def __init__(self, tokens):
        self.probabilitys = None
        self.ngrams = None
        self.tokens = tokens
        self.transition_dict = None
    
    def build_probability_dict(self):
        self.transition_dict = defaultdict(Counter)

        for i in range(len(self.tokens) - 1):
            self.transition_dict[self.tokens[i]][self.tokens[i+1]] += 1

        probability_dict = {}

        for word, following in self.transition_dict.items():
            total = sum(following.values())
            probability_dict[word] = {k: v/total for k, v in following.items()}

        return probability_dict


    def most_common_next(self, word):
        # pick out the most common word that follow input word
        most_common_word = self.transition_dict[word].most_common(1)[0][0]
            
        return most_common_word
    
    def generate_sentence(self, n, word):
        #init list and add first word to the sentence
        sentence = []
        sentence.append(word)
        
        for i in range(n):
            #genereate the next word and add to sentence
            next_word = self.weighted_random_choice(self.transition_dict[word])
            sentence.append(next_word)
            word = next_word

        return sentence
    
    import random

    def weighted_random_choice(self, choices):
        """
        Make a weighted random choice from a dictionary where the keys are the choices and the
        values are the weights.
        """
        total_prob = sum(choices.values())
        probs = [p / total_prob for p in choices.values()]
        chosen_key = np.random.choice(list(choices.keys()), p=probs)

        return chosen_key

 