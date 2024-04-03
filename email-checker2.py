import http.client

def validate_email(email):
    conn = http.client.HTTPSConnection("email-validator8.p.rapidapi.com")
    payload = "email=" + email.strip()
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'X-RapidAPI-Key': "5603e8e383mshc6325e6194c80b2p1dafacjsncf0d410e13b0",
        'X-RapidAPI-Host': "email-validator8.p.rapidapi.com"
    }
    conn.request("POST", "/api/v2.0/email", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

# Open the file containing emails
with open(r'C:\Users\morbi\OneDrive\Documents\GitHub\Python\emails.txt', 'r') as file:
    # Iterate over each line (email) in the file
    for email in file:
        validate_email(email)
