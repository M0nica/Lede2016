# this statement was used to test the document
# print("Classwork 05")

# API Application Programming Interface
# endpoint = URL your computer can visit

# REQUESTS API!
# docs - http://docs.python-requests.org/en/master/
# github -https://github.com/kennethreitz/requests

# must type 'pip install requests' in terminal
import requests
# response = requests.get('http://www.nytimes.com')
# print(response.text)

response = requests.get('https://api.spotify.com/v1/search?query=80s&type=playlist')

# use json to convert string that looks like a
# dictionary from a string to a real live dictionary!
data = response.json()
# print(response.text.keys())

print(data.keys())
print(type(data['playlists']))
print(data['playlists'].keys())
playlists = data['playlists']['items']
print(type(playlists))

# this prints out the name of each playlist in playlists!

for playlist in playlists:
    print(playlist['name'], playlist['href'])
