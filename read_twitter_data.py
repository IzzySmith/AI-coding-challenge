from collections import defaultdict
import pattern3
import nltk
from nltk.tokenize import word_tokenize
import gensim
import re
from string import punctuation


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
            sentances.append(clean_data(l[19:]))
    return sentances

#clean data

def clean_data(line):
    #TODO: tidy up
    translation = str.maketrans("", "", punctuation)
    without_retweet = line.replace('RT ', '', 1)
    without_urls = re.sub(r"http\S+", "", without_retweet)
    without_reference = re.sub(r"@\S+", "", without_urls)
    without_punct = without_reference.translate(translation)
    return word_tokenize(without_punct)       

tokenised_sentances = get_list_of_sentances('data_collected.txt')

#pass in min count parameter to ignore words that appear with low frequecy

model = gensim.models.Word2Vec(tokenised_sentances, min_count=10)
model.save('twittermodel')


