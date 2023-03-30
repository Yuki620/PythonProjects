from bs4 import BeautifulSoup
import requests
import lxml
import smtplib, ssl

password = 'generatedPassword'
context = ssl.create_default_context()
smtp_server = "smtp.gmail.com"
sender_email = "mygmail@gmail.com"
receiver_email = "mygmail@gmail.com"


url = "Amazon URL"
header = {
    "User-Agent": "from myhttp",
    "Accept-Language": "from myhttp",
    "Cookie":"from myhttp"
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
