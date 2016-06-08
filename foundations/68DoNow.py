import requests
url = "http://api.bubblegum.com/flavors/list.json?APIKEY=b335"
response = requests.get(url)
data = response.json
type(data)
data.key()
type(data['flavors'])
for flavor in data['flavors']:
  print(flavor)

url = "http://api.bubblegum.com/ca7/show.json"
response = request.get(url)
data = response.json()
type(data) #dict
data.keys() #id, name , popularity, flavors
if data['popularity'] > 100:
    print("Wow, that's popular")


flavors = data['flavors']
for flavor in flavors:
    print(flavor)
