import requests
import json

# Bitly API key
api_key = "7b54a242ece91b73eb0897a7bbafadfd60dba21f"

# Long URL
url = "https://stackoverflow.com/"

#Define short_url function
def short_url(data_json ):

    headers={'Authorization': f"{api_key}" }

    data = '{ "long_url": "'f"{url}"'" }'

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

    data_json = (response.json())
    
    print(data_json['link'])

# Define main function
def main():

# Call short_url function
    return short_url(data_json=())

if __name__ == "__main__":
    main()