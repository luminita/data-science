import sys
import json

def get_most_frequent_hashtags(filename):
    tweetsfile = open(filename)
    hashtags_frequencies = {}
    for line in tweetsfile:
        json_obj = json.loads(line)
        if "entities" in json_obj and "hashtags" in json_obj["entities"] and "text":
            hashtags = json_obj["entities"]["hashtags"]
            for ht in hashtags:
                if "text" in ht:
                    ht_text = ht["text"]
                    if ht_text in hashtags_frequencies:
                       hashtags_frequencies[ht_text] += 1
                    else:
                        hashtags_frequencies[ht_text] = 1                  

    return hashtags_frequencies.items()


def print_top_ten(hashtags):
    hashtags.sort(key=lambda p: p[1], reverse=True)
    for ht, fr in hashtags[0:10]:
        print ht, " ", fr


def main():
    tweet_file = sys.argv[1]

    hashtags = get_most_frequent_hashtags(tweet_file)

    print_top_ten(hashtags)
    
    
if __name__ == '__main__':
    main()
