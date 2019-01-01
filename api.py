import flask
import os 
import re
import requests
from dotenv import load_dotenv
from flask import request, jsonify
from prediction import predict
from textblob import TextBlob

load_dotenv()
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Sentiment Analysis - Twitter </h1>'''

@app.route('/sentiment', methods=['GET'])
def sentiment():
    # search_term = request.args.get('search_term')
    # sentiment_prediction = predict(search_term)
    # URL = "https://api.twitter.com/2/tweets/search/recent?query=tsla&tweet.fields=created_at&max_results=100"
    # BEARER_TOKEN = os.getenv('BEARER_TOKEN')
    # auth_token = "Bearer" + " " + BEARER_TOKEN
    # headers_auth = {"Authorization": auth_token}
    # r = requests.get(URL, headers=headers_auth)
    tweet = "RT @jenn_woodall: I do not care if NFTs ever become environmentally sustainable. I don\u2019t like the premise, and the idea of my art being bou\u2026"
    cleaned_tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    b = TextBlob(cleaned_tweet)
    print('tweet', tweet)
    print('cleaned_tweet', cleaned_tweet)
    print('sentiment: ', b.sentiment)
    # return r.json()
    return jsonify(b.sentiment)
app.run()
