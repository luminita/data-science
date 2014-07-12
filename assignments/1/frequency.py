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

def compute_frequencies(tweets):
    words = {}
    total = 0.0
    for tweet in tweets:
        for w in tweet.split():
            if w in words:
                words[w] += 1
            else:
                words[w] = 1
            total += 1.0
    frequencies = [(w, nw/total) for w, nw in words.iteritems()]
    frequencies.sort(key=lambda p: p[1])
    return frequencies

def print_frequencies(frequencies):
    for w, f in frequencies:
        print "{0} {1}".format(w.encode('utf-8'), f)
    
def main():
    tweet_file = sys.argv[1]

    all_tweets = get_tweets(tweet_file)
    frequencies_dict = compute_frequencies(all_tweets)    

    print_frequencies(frequencies_dict)


if __name__ == '__main__':
    main()
