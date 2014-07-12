# -*- coding: utf-8 -*-

import sys
import json 

def build_sentiment_dict(filename):
    afinnfile = open(filename)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores 

def get_tweets(filename):
    tweetsfile = open(filename)
    all_tweets = []
    i = 0
    for line in tweetsfile:
        json_obj = json.loads(line)
        if "text" in json_obj:
            all_tweets.append(json_obj["text"])
        else:
            i += 1
    #print i, len(all_tweets)
    return all_tweets

def calculate_emotions(sentiment_dict, all_tweets):
    emotions_scores = []
    for tweet in all_tweets:
        words = tweet.split()
        score = sum([sentiment_dict[w] for w in words if w in sentiment_dict])
        emotions_scores.append(score)
    return emotions_scores

def print_scores(all_tweets, emotions_scores):
    for (tw, es) in zip(all_tweets, emotions_scores):
        print es


def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]

    sentiment_dict = build_sentiment_dict(sent_file)
    all_tweets = get_tweets(tweet_file)
    
    emotions_scores = calculate_emotions(sentiment_dict, all_tweets)
    print_scores(all_tweets, emotions_scores)


if __name__ == '__main__':
    main()
