import requests
    
# Bitly API key.
api_key = "7b54a242ece91b73eb0897a7bbafadfd60dba21f"

# User input long URL.
url = input("Please enter a long URL: ")

# Validate user input URL.
def validate_url():
    check_url = requests.get(url)
    return check_url.status_code

# Generate short URL with Bitly.
def short_url(url):
    try:
        # Set API Key for Bitly.
        headers={'Authorization': f"{api_key}" }

        # Set URL input.
        data = '{ "long_url": "'f"{url}"'" }'

        # Request short URL response.
        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

        # Format response as json.
        shorl_url = (response.json()['link'])

        # Print short URL.
        print(f"The short URL is:\n{shorl_url}") 

    # If domain missing from URL, throw error.
    except KeyError:
        print("Invalid URL. Possibly no domain was provided. Please check the URL.")  

# Main
def main():
    try:   
        # If URL returns code 200 or 301, create short URL.
        if validate_url() == 200:
            return short_url(url)
        # If URL returns MissingSchema, fix URL schema and return short URL.
    except requests.exceptions.MissingSchema:
        return short_url("http" + "://" + url)
    except requests.exceptions.ConnectionError:
        # If connection cannot be established to the URL, throw error.
        print("Connection error. Please check the URL.")
main()