import flask
import os 
import requests
from dotenv import load_dotenv
from flask import request, jsonify
from prediction import predict
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
    URL = "https://api.twitter.com/2/tweets/search/recent?query=cupcakes&tweet.fields=created_at&max_results=100"
    BEARER_TOKEN = os.getenv('BEARER_TOKEN')
    auth_token = "Bearer" + " " + BEARER_TOKEN
    headers_auth = {"Authorization": auth_token}
    r = requests.get(URL, headers=headers_auth)
    return r.json()
app.run()
