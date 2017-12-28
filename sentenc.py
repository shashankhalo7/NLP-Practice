from nltk.book import *
import nltk
from nltk import word_tokenize
string = raw_input("Enter the data for sentence segmentation.After completion press enter")
sents = nltk.sent_tokenize(string)
print(sents)
