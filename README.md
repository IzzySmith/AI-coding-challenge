# AI-coding-challenge

### Goal

The main goal is to gain an insight into the way social media reacted to the Egypt terrorist attack on [date]. In order to do this, the Twitter API will be queried to collect tweets containing the words 'Egypt' and 'terrorism'. The data will be cleaned, and then the gensim Word2Vec model will be trained on this data. A website was created to allow users to query the model, and see the associations people have with terrorist attacks. 

### Data 

I queried the Twitter API with the filters 'Egpyt' and 'Terrorism'. This was restricted to the last 10 days, as, with a free basic account, I can only query a week time span. By collected data over 3 days I was able to extend this to 10 days.

The data was parsed to show 

`date, time: retweet or not, @user_name and text`

In total, over the 10 day period, 102,448 tweets were retrieved

The tweets were aranged as so:

`
2017-11-28 837
`

`
2017-11-27 4060
`

`
2017-11-26 15081
`

`
2017-11-25 28379
`

`
2017-11-24 32777
`

`
2017-11-23 156
`

`
2017-11-22 101
`

`
2017-11-21 21
`

`
2017-11-20 59
`

`
2017-11-19 114
`


Unsuprisingly, the majority of tweets were on the day the attack happened, with a drop off over the days following it.


### Model
##### Description and motivation

I used the Gensim word2vec model, https://radimrehurek.com/gensim/models/word2vec.html . This maps words in a vector space, connecting highly associated words together. It is based on the distributional hypothesis - words that appear in the same contexts share semantic meaning, https://www.tensorflow.org/tutorials/word2vec . I chose to use it because it is an effective technique to understand associations between words. 
