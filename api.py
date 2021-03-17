import flask
from flask import request, jsonify
from prediction import predict
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Sentiment Analysis - Twitter </h1>'''

@app.route('/sentiment', methods=['GET'])
def stock_info():
    search_term = request.args.get('search_term')
    sentiment_prediction = predict(search_term)
    return jsonify(sentiment_prediction)
app.run()