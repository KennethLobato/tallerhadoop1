import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    new = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet:
            text = tweet['text'].lower()
            sentiment = 0
            unknown = []
            for word in text.split():
                if word in scores:
                    sentiment = sentiment + scores[word]
                else:
                    unknown.append(word)
            score = sentiment / len(text.split())
            for word in unknown:
                if word in new:
                    new[word].append(score)
                else:
                    new[word] = [score]
    for word in new:
        mean = sum(new[word]) / float(len(new[word]))
        print "%s %f" %(word, mean)

if __name__ == '__main__':
    main()
