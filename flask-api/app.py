import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
    
# Bitly API key
api_key = "7b54a242ece91b73eb0897a7bbafadfd60dba21f"

# Long URL
url = "https://google.com/"

#Define short_url function
@app.route('/short_url')
def short_url():

# Set API Key for Bitly
    headers={'Authorization': f"{api_key}" }

# Set url input
    data = '{ "long_url": "'f"{url}"'" }'

# Request short url response
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

# Format response as json

    response_output = response.text

    json_loads = json.loads(response_output)

    output = json_loads['link']

    return {'result' : f"{output}"}

    
