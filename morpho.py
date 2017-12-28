from polyglot.text import Text, Word
from nltk.book import *
import nltk
from nltk import word_tokenize
words = ["preprocessing", "processor", "invaluable", "thankful", "crossed"]
for w in words:
  w = Word(w, language="en")
  print("{:<20}{}".format(w, w.morphemes))
