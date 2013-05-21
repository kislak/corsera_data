import sys
import urllib
import json

def lines(fp):
    print str(len(fp.readlines()))

def dict(fp):
    scores = {} # initialize an empty dictionary
    for line in fp:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores   

def score(fp, dict):
    for line in fp:
        j = json.loads(line)
        sum = 0
        if type(j) != type({}):
            continue
        t = j.get('text', '')

        for i in t.split(' '):
            sum = sum + dict.get(i, 0)
        print "sentiment:{0}".format(float(sum))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    d =  dict(sent_file)
    score(tweet_file, d)
  
#    print tws[1]

#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
