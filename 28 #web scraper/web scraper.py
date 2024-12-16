import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.whatmobile.com.pk/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    mobiles = soup.find_all('li', class_='product')
    with open('Mobile_Data.csv', mode='w', newline='', encoding='utf-8') as data:
        csv_writer = csv.writer(data)
        csv_writer.writerow(['Mobile Name', 'Price_PKR', 'Price_USD'])

        for mobile in mobiles:
            mobile_name = mobile.find('h4').text.strip().replace("\n", " ")

            price_pkr = mobile.find('span', class_='PriceFont').text.strip()

            usd_title = mobile.find('a')['title']
            price_usd = usd_title.split("USD")[-1].strip()

            csv_writer.writerow([mobile_name, price_pkr+"Rs", price_usd+"$"])

    print("Data has been successfully scraped and saved to 'Mobile_Data.csv")
else:
    print(f"Failed to retrieve the website. status code: {response.status_code}")