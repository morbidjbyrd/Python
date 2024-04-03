import requests

url = "https://whatsapp-osint.p.rapidapi.com/wspic/dck"

querystring = {"phone":"4026430166"}

headers = {
	"X-RapidAPI-Key": "5603e8e383mshc6325e6194c80b2p1dafacjsncf0d410e13b0",
	"X-RapidAPI-Host": "whatsapp-osint.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())