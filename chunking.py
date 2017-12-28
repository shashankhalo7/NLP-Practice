import nltk

def prepareForNLP(text):
	sentences = nltk.sent_tokenize(text)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	return sentences

def chunk(sentence):
	chunkToExtract = """
	NP: {<NNP>*}
		{<DT>?<JJ>?<NNS>}
		{<NN><NN>}"""
	parser = nltk.RegexpParser(chunkToExtract)
	result = parser.parse(sentence)
	for subtree in result.subtrees():
		if subtree.label() == 'NP':
			t = subtree
			t = ' '.join(word for word, pos in t.leaves())
			print(t)


sentences=prepareForNLP("This is a student of VIT Chennai")
sentences1=prepareForNLP("This is a cat")
sentences2=prepareForNLP("The horse as well as the rabbits which we wanted to keep has escaped")
sentences3=prepareForNLP("Making these decisions requires sophisticated knowledge of syntax")
n=input("Enter the number of sentence for POS tagging \n")
for i in range(0,n):

	data=raw_input("Enter a sentence \n")
	#sentence=prepareforNLP(data)
	#sentences.append(sentence)
	#print sentences

for sentence in sentences:
	e=chunk(sentence)
	print e
	print ("\n")
for sentence in sentences1:
	f=chunk(sentence)
	print f
	print ("\n")
for sentence in sentences2:
	g=chunk(sentence)
	print g
	print ("\n")
for sentence in sentences3:
	h=chunk(sentence)
	
	print h
	print ("\n")
