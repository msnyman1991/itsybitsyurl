import requests
from flask import Flask,render_template,request
import flask
import time

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
from requests.exceptions import RetryError

app = Flask(__name__)
# # Bitly API key.
api_key = "7b54a242ece91b73eb0897a7bbafadfd60dba21f"

@app.route('/')
def form():
    return render_template('form.html')

# Validate user input URL.
def validate_url():
    check_url = requests.get(request.form['shortenurl'])
    return check_url.status_code

# Generate short URL with Bitly.
@app.route('/', methods=["POST"])
def short_url():
    with app.app_context():
        try:
            if validate_url() == 200:
                # Get URL from form as user input
                url = request.form['shortenurl']
                    
                # Set API Key for Bitly.
                headers={'Authorization': f"{api_key}" }
                
                # Set URL input.
                data = '{ "long_url": "'f"{url}"'" }'

                # Request short URL response.
                response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

                # Format response as json.
                short_url_json = (response.json()['link'])

                # Return the short URL.
                #return f"The short URL is:\n{short_url_json}"
                env = Environment(loader=FileSystemLoader('templates'))
                tmpl = env.get_template('shortenurl.html')
                return flask.Response(tmpl.generate(result=short_url_json))
            else:
                return "ERROR"
        except requests.exceptions.ConnectionError:
                env = Environment(loader=FileSystemLoader('templates'))
                tmpl_err = env.get_template('error.html')
                return flask.Response(tmpl_err.generate(result="error"))