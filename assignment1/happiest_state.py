import sys
import json
import re

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
	score += 0.0
	#print text
	#print score
	
	#print dictResults.values()
	#print "count=" ,  count
	#for key, value in dictResults.items():
	#	value = value + 0.0
	#	#print key
	#	print value
	return text, score

def getLoc(line):
	place = []
	global state
	state = ""
	tweet = json.loads(line)
	try:
		#if tweet.has_key('lang'): 
		#	if tweet['lang'] == "en":
		if tweet.has_key('place'):
			if tweet['place'] != None:
				place = tweet['place']
				if place['country_code'] ==  "US":
					city, s=  place['full_name'].split(",")
					state = s.strip()
	except KeyError:
		return ""
	return state

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores = setScores(sent_file)
	stateScore = {}
	score = 0.0
	count = 0
	for line in tweet_file:
		st = getLoc(line)
		#print st
		if st <> "":
			text, score = assignSentiment(line, scores)
			score += 0.0
			#print st, score
			if stateScore.has_key(st):
				stateScore[st] +=  score + 0.0
			else:
				stateScore[st] = score
				
			
	for w in sorted(stateScore, key=stateScore.get, reverse=True):
		if len(w) == 2:
			print("%s" % (w.encode('utf-8').strip()))
			break

	

if __name__ == '__main__':
	main()
