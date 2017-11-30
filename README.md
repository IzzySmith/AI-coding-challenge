# AI-coding-challenge

### Goal

Sentiment Analysis of Twitter -> specifically looking at the setiment expressed towards the terrorist attack in Egypt 

Does the sentiment affect how long an item stays in the news?

Can we predict how long a story will stay relevant based on initial reaction?

### Data 

Queried the Twitter API with the filters 'Egpyt' and 'Terrorism'. This was restricted to the last 7 days, as, with a free basic account, I cannot query a longer time span.

The data was parsed to show 

`date, time: retweet or not, @user_name and text`

In total, over the 7 day period, 102,448 tweets were retrieved

### Model
##### Description and motivation

Gensim model word2vec https://radimrehurek.com/gensim/models/word2vec.html
