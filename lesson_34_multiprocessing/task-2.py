# Task 2
# Requests using concurrent and multiprocessing libraries
# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file. For this task use concurrent
# and multiprocessing libraries for making requests to Reddit API.


import requests

CLIENT_ID = '123'
SECRET_KEY = 'xxx'
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
data = {
    'grant_type': 'password',
    'username': 'user name',
    'password': 'password'
}
headers = {'User-Agent': 'MyAPI/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, headers=headers, data=data)
TOKEN = res.json()['access_token']
headers = {'User-Agent': 'MyAPI/0.0.1', 'Authorization': f'Bearer {TOKEN}'}
res = requests.get('https://www.reddit.com/api/v1/me', headers=headers)
print(res.json())

#http://universities.hipolabs.com/search?country=United+States&limit=5&offset=4