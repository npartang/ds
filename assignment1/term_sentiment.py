import sys
import json
import re
import string

def setScores(sentiment):
	#print str(len(sentiment.readlines()))
	scores = {} # empty dict
	for line in  sentiment:
		term,score = line.split("\t")
		scores[term] = int(score)
	#print scores.items()
	return scores

def checkMultipleWords(text, scores, score):
	#print "text in multi=", text
	complexkey = ""
	count = 0
	prevWord = ""
	words = text.split(" ")
	for word in words:
		if count == 0:
			prevWord = word
			#print "prevWord=" + prevWord
		else:
			complexkey = prevWord + " " + word
			#print complexkey
			prevWord = word
		count += 1
		if scores.has_key(complexkey):
			score = score + scores[complexkey]
	return score

def assignSentiment(line, scores):
	count = 0
	tweet= json.loads(line)
        try:
		text = tweet["text"]
        except KeyError:
                text = ""
	words = text.split(" ")
	count += 1
	score = 0
	for word in words:
		if scores.has_key(word):
			score = score + scores[word]
			#print word
		else:
			score = score + 0
		#check for complex keys
	score = checkMultipleWords(text, scores, score)
	#print text
	#print score
	
	#print dictResults.values()
	#print "count=" ,  count
	#for key, value in dictResults.items():
	#	value = value + 0.0
	#	#print key
	#	print value
	return text, score

def getAllTerms(tweets):
	allTermsUsed = []
	try:
		for tweet in tweets:
			#print tweet
			word = tweet.split()
			for eachword in word:
				#print tweet
				allTermsUsed.append(eachword)
				#print eachword
	except KeyError:
		pass
	return allTermsUsed


def removeUsedTerms(allTU, scores):
	newTerms = []
	try:
		for word in allTU:
			if scores.has_key(word):
				continue
			else:
				newTerms.append(word)
	except KeyError:
		pass
		
	return newTerms

def  scoreNew(nt, ts, scores):
	otherTerms = {item: [0,0] for item in nt}
	otherTermsScore = []
	try:
		for tweet in ts:
			#print tweet
			word = tweet.split()
			for eachword in word:
				#print ts[tweet]
				if scores.has_key(eachword):
					continue
				else:
					otherTerms[eachword][0] += ts[tweet]
					otherTerms[eachword][1] += 1.0
					#print otherTerms[eachword][0]
					#print otherTerms[eachword][1]
	except KeyError:
		pass
	try:
		otherTermsScore = {key: otherTerms[key][0]/otherTerms[key][1] for key in otherTerms}
	except ZeroDivisionError:
		pass
	return otherTermsScore

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores = setScores(sent_file)
	tweetScore = {}
	allTerms = {}
	for line in tweet_file:
		text, score = assignSentiment(line, scores)
		score += 0.0
		tweetScore[text] = score + 0.0
		#print score
	#for key in tweetScore:
	#	print key, tweetScore[key]
	allTerms = getAllTerms(tweetScore)
	#print allTerms
	newTerms = removeUsedTerms(allTerms, scores)
	#print newTerms
	#		
	remScore = scoreNew(newTerms, tweetScore, scores) 
	for key in remScore:
		print ("%s %s" %  (key.encode("UTF-8"), remScore[key]))
	

if __name__ == '__main__':
	main()
