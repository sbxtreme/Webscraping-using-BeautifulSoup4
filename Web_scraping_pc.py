# import pandas for creating dataframes
import pandas as pd
# importing the request library to request the data from the webpage
import requests
# importing beautifulsoup library
import bs4 as bs
r=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
#print(r.text[0:500])
# print(r.text)
# the below code is creating beautiful soup object
bso= bs.BeautifulSoup(r.text,'html.parser')
# start getting the text using find_all attr of beautiful soup 
results = bso.find_all('span', attrs={'class':'short-desc'})

#The above code can be rewritten as
#results = bso.find_all('span',class_='short-desc')

# print(len(results))
# # the type of this object is a beautiful soup object thus creating bs4 class internally.
# print(type(results))
# # the below code get the 1st 4 records/rows from the html source code from <spam> tag
# print(results[0:4])
# # the below code gets the last record/row from the html source code from <spam> tag
# print(results[-1])

# # to get the first object i.e date
# rec1= results[0]
# print(rec1)
# l=rec1.find('strong').string

# print(len(l))
# # to get the date
# rec1.find('strong').string[0:-1]

# # to get the second object i.e content
# rec1.contents[1][1:-2]

# # to get the third object i.e explaination
# rec1.find('a').text[1:-1]

# # to get the URl , bs treats the bs object as key value pair as in dictionaries so to get url below is the code.
# print(rec1.find('a')['href'])

# to get all the object using loop

output=[]
for i in results:
    d=i.find('strong').string[0:-1]+ ', 2017' # to get the date
    sc=i.contents[1][1:-2] # to get the second content
    tc=i.find('a').text[1:-1] # to get the third content
    url=i.find('a')['href'] # to get the url
    output.append((d,sc,tc,url)) # converting into tuple and appending in the list

#     # checking for 1st record which should be the combination of date,sc,tc and url
# print(output[0])

# converting the list into pandas dataframe and write in csv

df= pd.DataFrame(output,columns=['Date','Second_content','Third_content','URL'])
# convert into date format
df['Date']=pd.to_datetime(df['Date'])

df.head()

# creating the CSV file 
df.to_csv('Trump_lies.csv',index=False,encoding= 'utf-8')