import requests

url = "https://netdetective.p.rapidapi.com/query"

querystring = {"website":"162.159.135.42"}

headers = {
	"X-RapidAPI-Key": "5603e8e383mshc6325e6194c80b2p1dafacjsncf0d410e13b0",
	"X-RapidAPI-Host": "netdetective.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())