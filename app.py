import requests
import json
import requests
    
# Bitly API key
api_key = "7b54a242ece91b73eb0897a7bbafadfd60dba21f"

# Long URL
url = input("Please enter a long URL: ")
url_prefix = "http"

#request = requests.get(url)

def short_url(url):
     # Set API Key for Bitly
    headers={'Authorization': f"{api_key}" }

    # Set url input
    data = '{ "long_url": "'f"{url}"'" }'

    # Request short url response
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

    # Format response as json
    shorl_url = (response.json()['link'])

    print(f"The short URL is:\n{shorl_url}") 

def main():
    if url_prefix in url:
        return short_url(url)
    else:
        return short_url(f"{url_prefix}" + "://" + url)
main()

# To Do: 
# 1. Check if URL format is correct (Contains http// or https:// as prefix)
# 2. If URL format is incorrect, update url with http:// or https:// prefix
# 3. If URL format is correct, check if URL is reachable with status code 200
# 4. If URL format is correct and URL returns status code 200, generate short URL.