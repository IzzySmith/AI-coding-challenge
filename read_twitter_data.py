from collections import defaultdict
import pattern3
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import *
import gensim
import re
import string
#nltk.download('stopwords')
from nltk.corpus import stopwords
#nltk.download('averaged_perceptron_tagger')

stemmer = PorterStemmer()
stops = set(stopwords.words("english"))
punct = re.compile('[%s]' % re.escape(string.punctuation) + '|[0-9]|(:)|(rt )|@\S+|http\S+')

def get_date_dict(filename):
    with open(filename) as f:
	    lines = f.readlines()
	    date_dict = {}
	    dates = ['2017-11-19', '2017-11-20', '2017-11-21', '2017-11-22', '2017-11-23', '2017-11-24', '2017-11-25', '2017-11-26', '2017-11-27', '2017-11-28']
	    for l in lines:
	    	#need to make a list
	    	for d in dates:
	    		if d in l:
			    	date_dict.setdefault(d, []).append(l[21:])
	        
    return date_dict

data_dict = (get_date_dict('data_collected.txt'))

#for key, value in data_dict.items():
    #print value
    #print(key, len([item for item in value if item]))

def get_list_of_sentances(filename):
    with open(filename) as f:
        sentances = []
        lines = f.readlines()
        for l in lines:
            sentances.append(remove_unwanted_chars(l.lower()))
    return sentances

#clean data


def remove_unwanted_chars(line):
    #remobe stopwords
    text = ' '.join([word for word in line.split() if word not in stops])
    #remove punctuation, usernames, links, punctuation
    without_urls_number_retweet = punct.sub('', text)
    without_punct = without_urls_number_retweet.strip(string.punctuation)
    
    #remove the stopwords
    tokenised = word_tokenize(without_punct)
    return [stemmer.stem(t) for t in tokenised]

tokenised_sentances = get_list_of_sentances('data_collected.txt')
#print(tokenised_sentances)

#pass in min count parameter to ignore words that appear with low frequecy
model = gensim.models.Word2Vec(tokenised_sentances, min_count=10)
model.save('twittermodel')

#model = gensim.models.Word2Vec.load('twittermodel')

#model.most_similar('good')

