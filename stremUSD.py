from bs4 import BeautifulSoup
import urllib.request as req
import datetime

url = "https://finance.naver.com/marketindex/"
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')
currency = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print("Date: " + now + ' USD: ' + currency.string)