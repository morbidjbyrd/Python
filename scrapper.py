import http.client

conn = http.client.HTTPSConnection("website-contacts-scraper.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "5603e8e383mshc6325e6194c80b2p1dafacjsncf0d410e13b0",
    'X-RapidAPI-Host': "website-contacts-scraper.p.rapidapi.com"
}

conn.request("GET", "/scrape-contacts?query=prosperitylife.com&match_email_domain=false&external_matching=false", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))