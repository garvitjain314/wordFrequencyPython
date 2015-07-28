import sys
import re
def populateListOfWords(file,mode):
	f = open(file,mode)
	list = []
	for line in f:
		list += [x.lower() for x in re.findall(r"[\w]+", line)]
	return list

def displayWordFrequency(list, n):
	wordFrequencyPairList = sorted(set([(word,list.count(word)) for word in list]), key=lambda freq: freq[1], reverse=True)
	for item in wordFrequencyPairList[:n]:
		print(item, sep='\n')

list = populateListOfWords("in.txt", 'r')
numberOfWordsToDisplay = int(sys.argv[1])
displayWordFrequency(list, numberOfWordsToDisplay)