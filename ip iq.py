import requests

url = "https://ip-iq.p.rapidapi.com/ip"

querystring = {"ip":"162.159.135.42"}

headers = {
	"X-RapidAPI-Key": "5603e8e383mshc6325e6194c80b2p1dafacjsncf0d410e13b0",
	"X-RapidAPI-Host": "ip-iq.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())