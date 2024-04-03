import requests

url = "https://ics-ap-apis.p.rapidapi.com/advisory/latest"

querystring = {"n":"3"}

headers = {
	"X-RapidAPI-Key": "5603e8e383mshc6325e6194c80b2p1dafacjsncf0d410e13b0",
	"X-RapidAPI-Host": "ics-ap-apis.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())