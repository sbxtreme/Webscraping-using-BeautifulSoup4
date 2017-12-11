# #######################################################################################################
# The below code consists different print statements.To check the affect of each uncomment the statements 
# ########################################################################################################


import bs4 as bs
# the below library is used to make a request to the website on which webscaping needs to be done
import urllib.request
# importing a library pandas to convert the data into dataframes which is a kind of data structure.
import pandas as pd

# the below code extracts the HTML source code from the below website.
sc = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# the below code will create beautiful soup object with parser lxml
soup= bs.BeautifulSoup(sc,'lxml')

# print (sc)
# print (soup)
# print(soup.title)
# print(soup.title.string)
# print(soup.title.text)
# # the below is show 1st paragraph tag of the page from HTML source code
# print (soup.p)
# # the below will show all the paragraph tags present in the page.
# print (soup.find_all('p'))

# # the below code gets all the paragraph source code and fetch
# # only the text out of the paragraph tag
# for i in soup.find_all('p'):
# 	print (i.text)

# # if the data is not in paragraph tags and its under some others tags
# # like <pre> tags so to get the data from complete page we use below

# print (soup.get_text())

# # to get the urls mentioned in the page below can be used
# # here a is anchor tag used for hyperlinks in the page <a href>..</a>
# for i in soup.find_all('a'):
# 	print(i.get('href'))

# # the below code is used to get the links from the nav bar.
# print( soup.nav )
# nav= soup.nav
# for i in nav.find_all('a'):
# 	print(i.get('href'))

# # The below code is used to get the body data from a website.

# body= soup.body
# for i in body.find_all('p'):
# 	print(i.text)

# # In few of the websites it happens that the body text is in <div> tags so to get it below are the codes

# for i in soup.find_all('div',class_='body'):
# 	print(i.text)


# # The below code is used to parse the table structure present on the website.

# table = soup.table

# table_rows = table.find_all('tr')
# for i in table_rows:
# 	td = i.find_all('td')
# 	data=[i.text for i in td]
# 	print(data)

# # The below code is used to convert the tables into pandas dataframes.

# df= pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)
# for i in df:
# 	print(i)

# # The below code is used to parse XML present on the website
# # Example could be SITEMAPS, they contain all the links which are on the website.

sm = urllib.request.urlopen('https://www.washingtonpost.com/web-sitemap-index.xml').read()
soupsm= bs.BeautifulSoup(sm,'xml')

for i in soupsm.find_all('loc'):
	print(i.text)