__author__ = 'Peiman'
import nltk
#nltk.download()

#from nltk.book import *
x = 'welcome to my first sentiment analysis and natural language processing learning codes!.'

from nltk.tokenize import regexp_tokenize
tokenizer = regexp_tokenize(r'\w+')

tokenized = nltk.word_tokenize(x)
tagged = nltk.pos_tag(tokenized)
print tokenized
print tagged