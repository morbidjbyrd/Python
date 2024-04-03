import requests

url = "https://website-social-scraper-api.p.rapidapi.com/contacts/"

querystring = {"website":"https://www.prosperitylife.com/"}

headers = {
	"X-RapidAPI-Key": "5603e8e383mshc6325e6194c80b2p1dafacjsncf0d410e13b0",
	"X-RapidAPI-Host": "website-social-scraper-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())