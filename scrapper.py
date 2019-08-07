import urllib3
import requests
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
user_input = input("What you want to search on Amazon.in")
URL='https://www.amazon.in/s?k='+user_input
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content , 'html.parser')
title = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")
price = soup.find_all("span" , class_="a-price-whole")
for titles in title[:5]:
    print(titles.text)
