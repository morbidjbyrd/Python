import requests

url = "https://local-business-data.p.rapidapi.com/search"

querystring = {"query":"prosperitylife","limit":"20","lat":"37.775700","lng":"-122.395203","zoom":"13","language":"en","region":"us"}

headers = {
	"X-RapidAPI-Key": "5603e8e383mshc6325e6194c80b2p1dafacjsncf0d410e13b0",
	"X-RapidAPI-Host": "local-business-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())