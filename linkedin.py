import requests

url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"

querystring = {"linkedin_url":"www.linkedin.com/in/james-byrd-15a796259","include_skills":"false"}

headers = {
	"X-RapidAPI-Key": "5603e8e383mshc6325e6194c80b2p1dafacjsncf0d410e13b0",
	"X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())