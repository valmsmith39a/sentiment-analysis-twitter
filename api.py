import flask
import os 
import re
import requests
from dotenv import load_dotenv
from flask import request, jsonify
from prediction import predict
from fetch_services import fetch_tweets
from textblob import TextBlob

load_dotenv()
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Sentiment Analysis - Twitter </h1>'''

@app.route('/sentiment', methods=['GET'])
def sentiment():
    search_term = request.args.get('search_term')
    sentiment_prediction = predict(search_term)
    tweets = fetch_tweets(search_term)
    return tweets
   
app.run()
