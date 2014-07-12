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
        words_with_sentiments = [w for w in tweet.split() if w in sentiment_dict]
        scores = [float(sentiment_dict[w]) for w in words_with_sentiments]
        if scores:
            emotions_scores.append(sum(scores)/len(scores))
        else:
            emotions_scores.append(0)           
    return emotions_scores

def print_scores(all_tweets, emotions_scores):
    for (tw, es) in zip(all_tweets, emotions_scores):
        print es

def infer_terms(all_tweets, emotions_score, sentiment_dict):
    new_terms = {}
    for (tweet, score) in zip(all_tweets, emotions_score):
        new_words = [w for w in tweet.split() if w not in sentiment_dict]
        for nw in new_words:
            if nw in new_terms:
                new_terms[nw].append(score)
            else:
                new_terms[nw] = [score]
    for nw, l in new_terms.iteritems():
        print "{0} {1}".format(nw.encode('utf-8'), sum(l)/len(l))
                

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]

    sentiment_dict = build_sentiment_dict(sent_file)
    all_tweets = get_tweets(tweet_file)

    emotions_scores = calculate_emotions(sentiment_dict, all_tweets)
    infer_terms(all_tweets, emotions_scores, sentiment_dict)




if __name__ == '__main__':
    main()
