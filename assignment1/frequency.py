import sys
import json


#extracts the text of the tweets generated from twitterstream.py
def getTweetsFromFile(json_tweets_file_path):
	tweets = []
	with open(json_tweets_file_path) as f:
		lines = f.readlines()	
		for line in lines:
			tweet = json.loads(line)
			if ('text' in tweet):				
				tweets.append( tweet['text'].encode('utf-8') )
	return tweets


#returns a dictionary where the key is a word and 
#the value is the number of tweets containing that word
def getWordsOccurrences(tweets):
	occurrences = dict([])
	for tweet in tweets:
		words = set( tweet.split( ) ) #set is used to remove duplicates
		for word in words:
			if word in occurrences:
				occurrences[word] = occurrences[word] + 1
			else:
				occurrences[word] = 1
	return occurrences


def getFrequencies(tweets):
	occurrences = getWordsOccurrences(tweets)
	wordsCount = len(occurrences.keys())	
	for word in occurrences.keys():
		occurrences[word] = occurrences[word]/float(wordsCount)
	return occurrences
		

def main():
	tweets = getTweetsFromFile(sys.argv[1])
	frequencies = getFrequencies(tweets)
	for word in frequencies.keys():
		print word+" "+str(frequencies[word])


if __name__ == '__main__':
    main()
