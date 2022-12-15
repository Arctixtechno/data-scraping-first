# # from selenium import webdriver
# # from bs4 import BeautifulSoup
# # import pandas as pd
# # import time

# # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

# # products=[] #List to store name of the product
# # prices=[] #List to store price of the product
# # ratings=[] #List to store rating of the product
# # driver.get('<a href="https://khalidio.000webhostapp.com/">https://khalidio.000webhostapp.com/</a>')
# # time.sleep(1000)

# # content = driver.page_source
# # soup = BeautifulSoup(content)
# # print(soup)
# # # for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
# # # 	time.sleep(1000)
# # # 	name=a.find('div', attrs={'class':'_3wU53n'})
# # # 	price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
# # # 	rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
# # # 	products.append(name.text)
# # # 	prices.append(price.text)
# # # 	ratings.append(rating.text) 

# # # df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
# # # df.to_csv('products.csv', index=False, encoding='utf-8')

# # import webbrowser
# # webbrowser.open('https://khalidio.000webhostapp.com/', new=2)

# from bs4 import BeautifulSoup

# with open("index.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')

# soup = BeautifulSoup("<html>https://khalidio.000webhostapp.com/</html>", 'html.parser')

# print(soup)

from bs4 import BeautifulSoup
import requests
import csv

# source = requests.get('https://www.marketwatch.com/investing/stock/oonef').text

# soup = BeautifulSoup(source, 'lxml')

# # print(soup.prettify())

# titel = soup.find('li', class_='kv__item')
# price = titel.span.text
# print(price)

# for i in range(0,10):
# 	print()

source = requests.get('https://www.marketwatch.com/tools/markets/stocks/country/united-states').text
soup = BeautifulSoup(source, 'lxml')

# for list in soup.find('table', class_='table table-condensed'):
# 	stock = list.td.text
# 	print(stock)

# list = soup.find('tbody', class_='table table-condensed')

stocks_list = []
for list in soup.find_all('td', class_='name'):
	# stock = list.tr.text

	stockss = list.text
	for i in range(0, len(stockss)):
		if stockss[i] == '(':
			stocks_list.append(stockss[(i + 1):-1])


for i in range(0, len(stocks_list)):
	new_link = 'https://www.marketwatch.com/investing/stock/' + stocks_list[i].lower()
	new_source = requests.get(new_link).text
	new_soup = BeautifulSoup(new_source, 'lxml')

	stockname = new_soup.find('li', class_='kv__item')
	price = stockname.span.text
	with open('data_dump.csv', 'a', newline = '') as file:
		writer = csv.writer(file)
		writer.writerow([stocks_list[i], price])
	# print(f"The price of stock {stocks_list[i]} from it's website {new_link} is {price}\n")

# stocks_list = []
# brackets = False
# for i in range(0, len(stocks)):
# 	if stocks[i] == '(':
# 		brackets = True
# 	while brackets == True:
# 		if stocks[i + 1] == '(':
# 			brackets = False
# 		stocks_list.append(stocks[i + 1])

# print(stocks_list)
	

# stockname = list.td.text
# print(stockname)
