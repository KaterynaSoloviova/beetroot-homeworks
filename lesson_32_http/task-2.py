# Task 2
# Load data
# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file.
import json

import requests

url = "https://catfact.ninja/fact"

s = "y"

while s.lower() == "y":
    response = requests.get(url)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        print(json_data["fact"])
    else:
        print("Error requesting a date from the server. The server is unavailable.")
    s = input("Do you want to know more about cats (Y or N)? ")
