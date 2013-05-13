import sys
import urllib
import json

counter = 0

def score(fp):
    global counter
    dict = {}
    for line in fp:
        j = json.loads(line)
        sum = 0
        if type(j) != type({}):
            continue
        t = j.get('text', '')

        for i in t.split(' '):
            dict[i] = 1 + dict.get(i, 0)
            counter = counter + 1
    return dict

def main():
    tweet_file = open(sys.argv[1])
    dict = score(tweet_file)
    res = {}
    for k, v in dict.iteritems():
        print u"{0} {1}".format(k, float(v)/counter)
    
  
if __name__ == '__main__':
    main()
