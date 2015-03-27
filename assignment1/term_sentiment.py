import sys
import json



###############
# BASIC UTILS #
###############



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

def getTweetsTexts(json_tweets_file_path):
	jsonTweets = getTweetsFromFile(json_tweets_file_path)
	texts = []
	for tweet in jsonTweets:
		if 'text' in tweet:
			texts.append(tweet['text'])
	return texts



#####################
# PROBLEM FUNCTIONS #
#####################



#calculate the sentiment for a given tweet
def getSentimentScore(tweet, dictionary):
	sentimentScore = 0
	words = tweet.split( );
	for word in words:
		if word in dictionary:
			sentimentScore = sentimentScore + dictionary[word]
	return sentimentScore


#returns a dictionary where the key is a word and 
#the value is the number of tweets containing that word
def getWordsOccurrences(tweets):
	occurrences = {}
	for tweet in tweets:
		words = set( tweet.split( ) ) #set is used to remove duplicates
		for word in words:
			if word in occurrences:
				occurrences[word] = occurrences[word] + 1
			else:
				occurrences[word] = 1
	return occurrences


#update the new terms dictionary with the terms from the given tweet
def updateNewTermsDictionary(tweet, dictionary, advancedDictionary):
	tweetSentiment = getSentimentScore(tweet, dictionary)
	words = tweet.split( );
	for word in words:
		if word not in dictionary:
			if (tweetSentiment>0):
				if word in advancedDictionary:
					advancedDictionary[word] = advancedDictionary[word] + 1
				else:
					advancedDictionary[word] = 1
			if (tweetSentiment<0):
				if word in advancedDictionary:
					advancedDictionary[word] = advancedDictionary[word] - 1
				else:
					advancedDictionary[word] = -1


#the term frequency is used to calculate the sentiment score
def createTermFrequency(tweets):
	termFrequency = {}
	for tweet in tweets:
		words = tweet.split( );
		for word in words:
			if word not in termFrequency:
				termFrequency[word] = 1
			else:
				termFrequency[word] = termFrequency[word] +1
	for word in termFrequency.keys():
		termFrequency[word] = termFrequency[word]/float(len(termFrequency.items()))
	return termFrequency


#creates a sentiment dictionary for words not 
#containted in the original sentiment dictionary (AFINN-111.txt) 
def createNewTermsDictionary(tweets, dictionary):
	newTermsDictionary = {}
	for tweet in tweets:
		updateNewTermsDictionary(tweet, dictionary, newTermsDictionary)
	wordsOccurrences = getWordsOccurrences(tweets)
	termFrequency = createTermFrequency(tweets)
	#every term score is divided by the term occurrence
	for word in newTermsDictionary.keys():
		newTermsDictionary[word] = termFrequency[word]*newTermsDictionary[word] / float(wordsOccurrences[word])
	return newTermsDictionary



###############
# MAIN AND CO #
###############



def main():
	dictionary = getDictionaryFromFile(sys.argv[1])
	tweets = getTweetsTexts(sys.argv[2])
	newTermsDictionary = createNewTermsDictionary(tweets, dictionary)
	for item in newTermsDictionary.items():
		word = item[0]
	 	score = item[1]
	 	print word+" "+str(score)


if __name__ == '__main__':
    main()