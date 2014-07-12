import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def build_sentiment_dict(filename):
    afinnfile = open(filename)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def get_state(tweet_location):
    # if I find the name of the whole state, then it is clear
    for abbr, state in states.iteritems():
        if tweet_location.find(state) != -1:
            return abbr
    return None

def get_tweets(filename):
    tweetsfile = open(filename)
    all_tweets = {}
    for line in tweetsfile:
        json_obj = json.loads(line)
        if "text" in json_obj and "user" in json_obj and "location" in json_obj["user"] and json_obj["user"]["location"].strip() and "lang" in json_obj["user"] and json_obj["user"]["lang"] == 'en':
            state = get_state(json_obj["user"]["location"])
            if state:
                if state in all_tweets:
                    all_tweets[state].append(json_obj["text"])
                else:
                    all_tweets[state] = [json_obj["text"]]                   

    return all_tweets

def calculate_emotions(sentiment_dict, tweet):
    words = tweet.split()
    score = sum([sentiment_dict[w] for w in words if w in sentiment_dict])
    return score


def get_happiest_state(all_tweets, sentiment_dict):
    results = []
    for (state, tweets) in all_tweets.iteritems():
        scores = [calculate_emotions(sentiment_dict, t) for t in tweets]
        avg_score = sum(scores) / float(len(scores))
        results.append((state, avg_score))

    results.sort(key=lambda p:p[1], reverse=True)

    print results[0][0]
        
def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]

    sentiment_dict = build_sentiment_dict(sent_file)
    all_tweets = get_tweets(tweet_file)

    get_happiest_state(all_tweets, sentiment_dict)


    
if __name__ == '__main__':
    main()
