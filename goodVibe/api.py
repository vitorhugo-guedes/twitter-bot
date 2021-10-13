import requests
import json

URL = 'https://zenquotes.io/api/random'

def getQuote():
    response = requests.get(URL);
    data = json.loads(response.text);
    quote = data[0]['q'] + " --" + data[0]['a'];
    return quote









