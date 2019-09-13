# Sentiment Analysis
In order to carry out sentiment analysis, generally the following needs to be done:
- Get hold of training data
- Use a classifier (Naive Bayes, Random Forest)
- Extract features (tokenize, remove stop words, stem etc)
- Train into positive or negative

Use the trained model on test data.

## Try in Python
### Create Virtual Environment (optional)
Shell:
```
python3 -m venv sentiment
source ./bin/activate
```

### Dependencies
Shell:
```
pip3 install requests textblob
python3 -m textblob.download_corpora
```

### Analyse
We will analyse two reviews [for the movie Avatar from metacritic](https://www.metacritic.com/movie/avatar). Observe the results in both cases.

REPL:
```
>>> from textblob import TextBlob

>>> text1 = "You have to be kidding. The movie was awful and long. No suspense as the acting was bad. All the fancy colors and sounds were for kids with ADD. Much ado about nothing. Overhyped by the professional shills."
>>> TextBlob(text1).polarity
```

REPL:
```
>>> from textblob import TextBlob

>>> text2 = "Literally the best movie I have ever seen. I was completely and totally blown away. This is the first movie in my entire life where I didn't want it to end."
>>> TextBlob(text2).polarity
```

## Analyse Tweets
Create a file called `tweets_sentiment.py` and copy the following
```python
import re 
import tweepy 
from auth import api_key, api_secret_key, access_token, access_token_secret
from textblob import TextBlob 
from termcolor import colored

tweepy_auth = tweepy.OAuthHandler(api_key, api_secret_key) 
tweepy_auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(tweepy_auth) 

regex = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"

fetched_tweets = api.search(q = 'trump', count = 100) 

tweets = []
for tweet in fetched_tweets:
    if tweet.retweet_count > 0:
        if tweet.text not in tweets:
            tweets.append(tweet.text)
            clean_tweet = re.sub(regex, '', tweet.text)
            analysis = TextBlob(clean_tweet)
            color = 'red' if analysis.polarity < 0  else 'green' if analysis.polarity > 0 else 'yellow'
            print(tweet.text, '(', colored(analysis.polarity, color), ')')

```
Create another file called `auth.py` and copy the following
```python
api_key = ''
api_secret_key = ''
access_token = ''
access_token_secret = ''
```
Update the above with twitter api credentials.

Run it in shell
```shell
python3 tweets_sentiment.py
```