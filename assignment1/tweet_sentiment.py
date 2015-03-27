import sys
import json


def getDictionaryFromFile(terms_file_path):
	termsFile = open(terms_file_path)
	scores = {}
	for line in termsFile:
	  term, score  = line.split("\t")
	  scores[term] = int(score)
	return scores


def getTweetsFromFile(json_tweets_file_path):
	jsons = []
	with open(json_tweets_file_path) as f:
		lines = f.readlines()	
		for line in lines:
			jsons.append( json.loads(line) )
	return jsons


def getSentiment(tweet, dictionary):
	words = tweet['text'].encode('utf-8').split( )
	score = 0
	for word in words:
		if word in dictionary:
			score = score + dictionary[word]
	return score


def printSentiments(tweets, dictionary):
	for tweet in tweets:	
		if 'text' not in tweet: #this is for 'other types of streaming messages'
			print ""
		else:	
			print str(getSentiment(tweet, dictionary))


def main():
	dictionary = getDictionaryFromFile(sys.argv[1])
	tweets = getTweetsFromFile(sys.argv[2])
	printSentiments(tweets, dictionary)
	

if __name__ == '__main__':
    main()
