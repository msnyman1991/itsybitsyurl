import requests
import json
from flask import Flask
app = Flask(__name__)
    
# Bitly API key
api_key = "7b54a242ece91b73eb0897a7bbafadfd60dba21f"

# Long URL
url = "https://stackoverflow.com/"

#Define short_url function
@app.route('/')
def short_url():

# Set API Key for Bitly
    headers={'Authorization': f"{api_key}" }

# Set url input
    data = '{ "long_url": "'f"{url}"'" }'

# Request short url response
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

# Format response as json
    response_json = (response.json())

# Filter json response     
    response_json_filterd = print(response_json['link'])

# Convert filtered json response to string
    url_string = print(str(response_json_filterd))

    return short_url()
    
# Define main function
# def new():

# # Call short_url function
#     return short_url(url_string=())

# def main():
    
#     return new()

if __name__ == "__main__":
    app.run()