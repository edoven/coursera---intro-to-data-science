import sys
import json

def createTermDictionary(terms_file_path):
	termsFile = open(terms_file_path)
	scores = {} # initialize an empty dictionary
	for line in termsFile:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	return scores


def getJsonTweets(json_tweets_file_path):
	jsons = []
	with open(json_tweets_file_path) as f:
		lines = f.readlines()	
		for line in lines:
			jsons.append( json.loads(line) )
	return jsons


def getSentiment(tweet, dictionary):
	if ('text' not in tweet): #this is for 'other types of streaming messages'
		return "#"
	words = tweet['text'].encode('utf-8').split( )
	score = 0
	for word in words:
		if word in dictionary:
			score = score + dictionary[word]
	return score


def main():
	dictionary = createTermDictionary(sys.argv[1])
	tweets = getJsonTweets(sys.argv[2])

	for tweet in tweets:		
		print str(getSentiment(tweet, dictionary))


if __name__ == '__main__':
    main()