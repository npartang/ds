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


def getAllTags(tweet_file):
	tagResults = []
	for line in tweet_file:
		tweet = json.loads(line[:-1], encoding='utf-8')
		try:
			tags = tweet['entities']['hashtags']
			if len(tags) == 0:
				continue
			else:
				for tag in tags:
					tagResults.append(tag['text'])
		except KeyError:
			pass
	uniqueTags = set(tagResults)

	tags_observed = {item: 0.0 for item in uniqueTags}
	count = 0.0
	for word in tagResults:
		try:
			tags_observed[word] += 1
		except KeyError:
			pass
	
	finalTags = {key: tags_observed[key] for key in tags_observed}
			
	#for key in finalTags:
	#	print key, finalTags[key]			
	count=0
        for w in sorted(finalTags, key=finalTags.get, reverse=True):
                        if count == 10:
                                break
                        else:
                                print("%s %s" % (w.encode("UTF-8"), finalTags[w]))
                                count += 1
				

	

def main():
	
	sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
	tweet_file = open(sys.argv[1])
	tags = getAllTags(tweet_file)

if __name__ == '__main__':
	main()
