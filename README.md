

# Project Name: Similarity Checker

## Description
The Similarity Checker is a Python program that uses the spaCy library to compare the similarity between words. The program takes a list of words as input, and compares each word with every other word in the list. For each comparison, the program calculates the similarity score between the two words, and displays it to the user. 

This program is useful for anyone who wants to quickly compare the similarity between multiple words. It could be used by linguists, researchers, and writers to identify common patterns or themes across a set of words.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation
To run this program, you will need to have Python installed on your computer. You will also need to install the spaCy library by running the following command in your terminal:

`pip install spacy`

Once you have installed spaCy, you will need to download a language model. This program was built using the 'en_core_web_md' model, but you can also use the smaller 'en_core_web_sm' model if you prefer. To download the 'en_core_web_md' model, run the following command in your terminal:

`python -m spacy download en_core_web_md`

To download the 'en_core_web_sm' model, run the following command in your terminal:

`python -m spacy download en_core_web_sm`

## Usage
To use this program, open the 'similarities.py' file in your Python editor of choice. Modify the 'words' list to include the words that you want to compare. Then, run the program by clicking the 'Run' button or by typing the following command in your terminal:

`python similarities.py`

The program will output the similarity score for each pair of words in the 'words' list. 

If you want to modify the language model used by the program, simply change the line of code that loads the model. For example, if you want to use the 'en_core_web_sm' model instead of the 'en_core_web_md' model, change the following line of code:

`nlp = spacy.load('en_core_web_md')`

to:

`nlp = spacy.load('en_core_web_sm')`

## Credits
This program was created by Nazila zadeh
