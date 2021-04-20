import os
import requests

def fetch_tweets(search_term):
    BEARER_TOKEN = os.getenv('BEARER_TOKEN')
    auth_token = "Bearer" + " " + BEARER_TOKEN
    headers_auth = {"Authorization": auth_token}
    base_url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = "?query=" + search_term + "&tweet.fields=created_at&max_results=100"
    URL = base_url + query_params
    r = requests.get(URL, headers=headers_auth)
    return r.json()
