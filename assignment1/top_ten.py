import sys
import json
import operator

def getJsonTweets(json_tweets_file_path):
	jsons = []
	with open(json_tweets_file_path) as f:
		lines = f.readlines()	
		for line in lines:
			jsons.append( json.loads(line) )
	return jsons


def getHashtagToOccurrences(tweets):
	hashtags2occurrences = {}	
	for tweet in tweets:
		if ('text' in tweet):
			hashtags = tweet['entities']['hashtags']
			for hashtagEntity in hashtags:
				hashtag = hashtagEntity['text']
				if hashtag in hashtags2occurrences.keys():
					hashtags2occurrences[hashtag] = hashtags2occurrences[hashtag] +1
				else:
					hashtags2occurrences[hashtag] = 1							 
	return hashtags2occurrences


def getTop10Hashtags(tweets):
	hashtags2occurrences = getHashtagToOccurrences(tweets)
	hashtags2occurrences = sorted(hashtags2occurrences.items(), key=operator.itemgetter(1), reverse=True)
	return hashtags2occurrences[:10]
	
	
def main():
	tweets = getJsonTweets(sys.argv[1])
	top10hashtags = getTop10Hashtags(tweets)
	for i in range(0,10):
		hashtag = top10hashtags[i]
		print hashtag[0]+" "+str(hashtag[1])
	

if __name__ == '__main__':
    main()
