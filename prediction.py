def predict(data):
    # call prepare_data
    # twitter API 
    # return prediction result
    # tweet = "RT @jenn_woodall: I do not care if NFTs ever become environmentally sustainable. I don\u2019t like the premise, and the idea of my art being bou\u2026"
    # cleaned_tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    # b = TextBlob(cleaned_tweet)
    # print('tweet', tweet)
    # print('cleaned_tweet', cleaned_tweet)
    # print('sentiment: ', b.sentiment)
    # return r.json()
    # return jsonify(b.sentiment)                  
    return { 'id': '01', 'search_term': data, 'result': 'negative' } 