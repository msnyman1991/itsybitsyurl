import requests
from flask import Flask,render_template,request
import flask
import time

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

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


# Main
# @app.route('/', methods = ['POST', 'GET'])
# def main():
#     try:
#         with app.test_request_context():
#         # If URL returns code 200 or 301, create short URL.
#             if request.method == 'POST':
#                 #return render_template('shortenurl.html', shortcode=request.args['shortcode'])
#                 return short_url()
#         # If URL returns MissingSchema, fix URL schema and return short URL.
#     # except requests.exceptions.MissingSchema:
#     #     return short_url("http" + "://" + url)
#     except requests.exceptions.ConnectionError:
#         # If connection cannot be established to the URL, throw error.
#         return 'Connection error. Please check the URL.'
# main()

# @app.route('/')
# def my_form():
#     return render_template('form.html')

# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text