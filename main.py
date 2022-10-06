from bs4 import BeautifulSoup
import xml
import requests
from twilio.rest import Client

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 "
                  "Safari/537.36 Edg/105.0.1343.50",
    "Accept-Language": "en-US,en;q=0.9",

}

url = "https://www.amazon.com/PlayStation-5-Console/dp/B09DFCB66S/ref=sr_1_4?crid=XADKYEUE3BBO&keywords=ps5&qid" \
      "=1665068500&qu=eyJxc2MiOiI2LjgzIiwicXNhIjoiOC42MSIsInFzcCI6IjguMDkifQ%3D%3D&sprefix=ps5%2Caps%2C1465&sr=8-4 "

response = requests.get(url, headers=headers)
amazon_site = response.text

soup = BeautifulSoup(amazon_site, 'html.parser')
price_tag = soup.find(name="span", class_="a-offscreen")
price_of_ps5 = float((price_tag.text.strip("$")))

if price_of_ps5 < 400:
    account_sid = "ACc87e71b0432c983f32485d10b5d0f9fd"
    auth_token = "2ba3267cf82f5aebee56ef87896d0341"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f" The price of PS5 has dropped to {price_of_ps5} buy it ASAP.",
        from_='+00000000000',
        to='your number'
    )

    print(message.status)
