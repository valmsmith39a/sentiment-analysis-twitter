import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

sample_stock_info = {
    'ticker': 'TSLA',
    'name': 'Tesla, Inc',
    'closingPrice': '688.89',
    'pe': '1025.24'
}

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Stock Data</h1>'''

@app.route('/stocks/single/data/all', methods=['GET'])
def stock_info():
    return jsonify(sample_stock_info)
app.run()