import http.client

def validate_email(email):
    conn = http.client.HTTPSConnection("email-validator8.p.rapidapi.com")

    payload = f"email={email}"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'X-RapidAPI-Key': "5603e8e383mshc6325e6194c80b2p1dafacjsncf0d410e13b0",
        'X-RapidAPI-Host': "email-validator8.p.rapidapi.com"
    }

    conn.request("POST", "/api/v2.0/email", payload, headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")

    return data

def main():
    with open(r'C:\Users\morbi\OneDrive\Documents\GitHub\Python\emails.txt', 'r') as file:
        emails = file.readlines()

    for email in emails:
        email = email.strip()  # Remove leading/trailing whitespace and newline characters
        response = validate_email(email)
        if 'valid' in response:
            print(f"{email} is valid.")
        else:
            print(f"{email} is not valid.")

if __name__ == "__main__":
    main()
