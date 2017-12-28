from nltk.book import *
import nltk
from nltk import word_tokenize
string = raw_input("Enter the string for POS tagging")
text = word_tokenize(string)
print(nltk.pos_tag(text))
