import sys
import json
import codecs

def setScores(sentiment):
	#print str(len(sentiment.readlines()))
	scores = {} # empty dict
	for line in  sentiment:
		term,score = line.split("\t")
		scores[term] = int(score)
	#print scores.items()
	return scores


def computeFrequency(tweet_file):
	dictResults = {}
	for line in tweet_file:
		#print "*************************"
		pyresponse= json.loads(line)
		#print pyresponse.keys()
		#print type(line)
		if pyresponse.has_key("text"):
			text = pyresponse["text"]
		else:
	 		continue
		#if pyresponse.has_key("lang"):
		#	lang = pyresponse["lang"]
		#	if lang == "en":
		#now parse the text and add up the terms
		words = text.split()
		for word in words:
			if dictResults.has_key(word):
				dictResults[word] = dictResults[word] + 1
			else:
				dictResults[word] = 1
	
	#for key, value in dictResults.items():
		#print "word=", key, ":", "count=", value
	totalTermCount = 0
	for value in dictResults.values():
		totalTermCount = totalTermCount + value	+ 0.0
	totalTermCount = totalTermCount 
	#print "# of occurrences of all terms in all tweets=", totalTermCount
	#compute term frequency
	#try:
	for key, value in dictResults.items():
		print("%s %s" % (key.encode("UTF-8"),round(value/totalTermCount, 4)))
	#except UnicodeEncodeError:
	#	pass
def main():
	
	sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
	tweet_file = open(sys.argv[1])
	computeFrequency(tweet_file)

if __name__ == '__main__':
	main()
