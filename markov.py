# The code reads a text file, removes punctuation, and builds a Markov model dictionary. 
# Then, it uses the Markov model to predict a sequence of words starting from a given word.

#Markov model dictionary captures the  statistical patterns of word transitions in the given input text. 
# It can be used to generate text based on the probabilities of word occurrences in the original text.

from collections import defaultdict
import string
import random

class Markov():
    def __init__(self, file_path):
        self.file_path = file_path
        
        self.text = self.remove_punctuations(self.get_text())
        self.model = self.model()
        
    def get_text(self):
        text = []
        for line in open(self.file_path):
            text.append(line)
        return ' '.join(text)
    
    def remove_punctuations(self, text):
        return text.translate(str.maketrans('','', string.punctuation))
    
    # Suppose we have the following text:
    # text = "I like to eat apples. I like to eat bananas. I like to eat oranges."
    # We want to build a Markov model dictionary that looks like this:
    # markov_dict = {
    #"I": ["like", "like", "like"],
    #"like": ["to", "to", "to"],
    #"to": ["eat", "eat", "eat"],
    #"eat": ["apples.", "bananas.", "oranges."],
    #"apples.": ["I"],
    #"bananas.": ["I"],
    #"oranges.": ["I"]
    
    def model(self):
        words = self.text.split(' ')

        markov_dict = defaultdict(list)

        for current_word, next_word in zip(words[0:-1], words[1:]):
            markov_dict[current_word].append(next_word)

        markov_dict = dict(markov_dict)
        print('Successfully Trained')
        return markov_dict
  
# chain is the the Markov model dictionary   
# first_word is the word to start the prediction
# number_of_words is the number of words to predict  
    
def predict_words(chain, first_word, number_of_words=5):
    if first_word in list(chain.keys()): # check if the first word is in the Markov model dictionary
        word1 = str(first_word)
        
        predictions = word1.capitalize()

        for i in range(number_of_words-1):
            word2 = random.choice(chain[word1])
            word1 = word2
            predictions += ' ' + word2

        predictions += '.'
        return predictions
    else:
        return "Word is not in the dictionary."
    
if __name__ == '__main__':
    m = Markov(file_path='trainingData.txt')
    chain = m.model
    print(predict_words(chain, first_word = 'I', number_of_words = 5))