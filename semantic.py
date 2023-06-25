#This program foundfinds what is is  interesting about the similarities
#between cat, monkey and banana and I add an example of my own.
#Then Runs the example file with the simpler language model ‘en_core_web_sm’ and
#I have  writen what is different from the model 'en_core_web_md'and en_core_web_sm

import spacy

# Load the large English NLP model
nlp = spacy.load('en_core_web_md')

# Define a function to print the similarities between two words
def print_similarity(word1, word2):
    token1 = nlp(word1)
    token2 = nlp(word2)
    similarity = token1.similarity(token2)
    print(f"The similarity between '{word1}' and '{word2}' is {similarity:.2f}")

# Define a list of words to compare
words = ['cat', 'monkey', 'banana']

# Loop through the list and compare each word with every other word
for i in range(len(words)):
    for j in range(i+1, len(words)):
        print_similarity(words[i], words[j])
        
''''# Write a note about what you found interesting about the similarities between cat, monkey and banana and think of an example of your own.
print(' found it interesting that the similarity between 'cat' and 'monkey' is higher than the similarity between 'cat' and 'banana'. 
      This could be because cats and monkeys are both animals that are often kept as pets or companions,
        while bananas are a type of fruit. An example of my own could be comparing the similarities between different types of flowers based on their color or shape.
        ')
'''
# Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on what you notice is different from the model 'en_core_web_md'
nlp_sm = spacy.load('en_core_web_sm')
doc = nlp_sm(" how wonderfull, this is summer")
for token in doc:
    print(token.text, token.pos_, token.dep_)

   #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
   # For example, en_core_web_sm is a small English pipeline trained on written web text (blogs, news, comments), that includes vocabulary, syntax and entities.
   # for example, en_core_web_md is a medium-sized English model trained on written web text (blogs, news, comments), that includes a tagger, 
   # a dependency parser, a lemmatizer, a named entity recognizer and a word vector table with 20k unique vectors.
   #---------------------------------------------------------------------------------------------------------------------------------------------------------------------