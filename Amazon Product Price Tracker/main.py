from bs4 import BeautifulSoup
import requests
import lxml
import smtplib, ssl

password = 'fkwjstuqogtnebmt'
context = ssl.create_default_context()
smtp_server = "smtp.gmail.com"
sender_email = "20yuchi@gmail.com"
receiver_email = "20yuchi@gmail.com"


url = "https://www.amazon.com/Apple-Watch-Midnight-Aluminum-Always/dp/B0BDJBG74R/ref=sr_1_1_sspa?crid=77PVQ17ZC5OH&keywords=apple+watch+series+8&qid=1680106184&sprefix=apple+watch+ser%2Caps%2C159&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.ac2169a1-b668-44b9-8bd0-5ec63b24bcb5&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExVzQwWEtTWDRRNVomZW5jcnlwdGVkSWQ9QTAwMTU5OThFUDBVMUZBSkhOVEMmZW5jcnlwdGVkQWRJZD1BMDc3NzMzMFZETFZZNjJCRkQ5MiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie":"_ga=GA1.2.1166338422.1680106292; _gid=GA1.2.748138662.1680106292; PHPSESSID=ec2c404861ed1c563355faab328e3c88"
}

response = requests.get(url, 
               headers=header)
amazon = response.content
soup = BeautifulSoup(amazon, "lxml")

price = soup.find(name="span", class_="a-price-whole")
cents = soup.find(class_="a-price-fraction")
money = [price.get_text(), cents.get_text()]
price = "".join(money)
product = soup.find(id="productTitle").getText().strip()

message = f"""\
Subject: Amazon Price Alert!


{product} has dropped below the target to ${price}!
{url}
"""

target_price = 250

if float(price) <= target_price:
    with smtplib.SMTP(smtp_server, port=587) as server:
        server.starttls()
        result = server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
