# AI-coding-challenge

### Goal

Sentiment Analysis of Twitter -> specifically looking at the setiment expressed towards the terrorist attack in Egypt 

Does the sentiment affect how long an item stays in the news?

Can we predict how long a story will stay relevant based on initial reaction?

### Data 

Queried the Twitter API with the filters 'Egpyt' and 'Terrorism'. This was restricted to the last 10 days, as, with a free basic account, I can only query a week time span. By collected data over 3 days I was able to extend this to 10 days.

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

### Model
##### Description and motivation

Gensim model word2vec https://radimrehurek.com/gensim/models/word2vec.html
