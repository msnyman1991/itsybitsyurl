import requests
from flask import Flask,render_template,request

app = Flask(__name__)
# # Bitly API key.
api_key = "7b54a242ece91b73eb0897a7bbafadfd60dba21f"

@app.route('/')
def form():
    return render_template('form.html')

# User input long URL.
#url = input("Please enter a long URL: ")

# Validate user input URL.
# def validate_url():
#     check_url = requests.get(url)
#     return check_url.status_code

# Generate short URL with Bitly.
@app.route('/', methods=["POST"])
def short_url():
        url = request.form['shortenurl']
    #try:
        with app.app_context():
            
            # Set API Key for Bitly.
            headers={'Authorization': f"{api_key}" }
            
            # Set URL input.
            data = '{ "long_url": "'f"{url}"'" }'

            # Request short URL response.
            response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

            # Format response as json.
            short_url_json = (response.json()['link'])

            # Return the short URL.
            return f"The short URL is:\n{short_url_json}"
    # If domain missing from URL, throw error.
    # except KeyError:
    #     return 'Invalid URL. Possibly no domain was provided. Please check the URL.' 

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