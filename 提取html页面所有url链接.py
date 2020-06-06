from bs4 import BeautifulSoup
import requests
r=requests.get('https://python123.io/ws/demo.html')
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
