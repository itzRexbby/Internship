#!/usr/bin/env python
# coding: utf-8

# #                                             Web Scraping

# 
# # Question 1

# In[3]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
url='https://www.imdb.com/list/ls056092300/'


# In[4]:


response=requests.get(url)


# In[5]:


response


# In[6]:


soup=BeautifulSoup(response.content)
soup


# In[7]:


titles = []
for item_header in soup.find_all('h3', class_='lister-item-header'):
    title = item_header.find('a').text.strip()
    titles.append(title)

print(titles)


# In[8]:


rating=[]
for i in soup.find_all('span',class_="ipl-rating-star__rating")[::23]:
    rating.append(i.text.strip())
rating


# In[10]:


release=[]
for i in soup.find_all('span',class_="lister-item-year text-muted unbold"):
    release.append(i.text)
release


# In[11]:


df=pd.DataFrame({"Title ":titles,"Release ":release,"Rating":rating},index=range(1,len(titles)+1))
df


# # Question 2

# In[13]:


url='https://peachmode.com/pages/search?q=bags'
response=requests.get(url)
response


# In[14]:


soup=BeautifulSoup(response.content)
soup


# In[18]:


names=[]
for i in soup.find_all('span',class_="si-fname si-text"):
    names.append(i.text)
print(names)


# In[114]:


discount=[]
for i in soup.find_all('div',class_="product-tags sale"):
    discount = item_header.find('a').text.strip()
    discount.append(title)
    
discount


# # Question 3

# In[87]:


url = "https://www.icc-cricket.com/rankings/team-rankings/mens/odi"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")



# In[88]:


team_data = []
table = soup.find("div")
print(table)


# In[89]:


rows = table.find_all("tr")

for row in rows[1:11]:
  cells = row.find_all("td")
  team = cells[1].text.strip()
  matches = cells[2].text.strip()
  points = cells[3].text.strip()
  rating = cells[4].text.strip()
  team_data.append([team, matches, points, rating])

df = pd.DataFrame(team_data, columns=["Team", "Matches", "Points", "Rating"])
print(df)


# 
# 

# # QUESTION 4
# 

# In[92]:


url="https://www.patreon.com/coreyms"
import regex as re
response=requests.get(url)
response


# In[93]:


soup=BeautifulSoup(response.text,'html.parser')
soup


# In[94]:


title=[]
for i in soup.find_all('span',class_="sc-1cvoi1y-0 hxhWXn"):
    title.append(i.text)
print(title)


# In[100]:


title=soup.find('a',{'data-tag':'post-title'})
a=title.find('a')
print(a)


# In[84]:


span_element = soup.find('span', class_='sc-1cvoi1y-0 hxhWXn')

# Extract the title text
title = span_element

print(title)


# NOTE-------NOTE------NOTE---------NOTE----------NOTE----------NOTE-------NOTE------NOTE---------NOTE--
# 
# This site isnt giving me span or div of the posts after the patreon membership section. I tried multiple approach even tried every class still its no luck!!!

# # QUESTION 5 

# In[231]:


url="https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45OTgxNzMyLCJsb24iOjc3LjU1MzA0NDU5OTk5OTk5LCJwbGFjZUlkIjoiQ2hJSnhmVzREUE05cmpzUktzTlRHLTVwX1FRIiwicGxhY2VOYW1lIjoiUmFqYWppbmFnYXIifSx7ImxhdCI6MTIuOTMwNzczNSwibG9uIjo3Ny41ODM4MzAyLCJwbGFjZUlkIjoiQ2hJSjJkZGxaNWdWcmpzUmgxQk9BYWYtb3JzIiwicGxhY2VOYW1lIjoiSmF5YW5hZ2FyIn0seyJsYXQiOjEyLjk3ODM2OTIsImxvbiI6NzcuNjQwODM1NiwicGxhY2VJZCI6IkNoSUprUU4zR0tRV3Jqc1JOaEJRSnJoR0Q3VSIsInBsYWNlTmFtZSI6IkluZGlyYW5hZ2FyIn1d&radius=2.0&city=bangalore&locality=Rajajinagar,Jayanagar,Indiranagar"


# In[232]:


response=requests.get(url)
response


# In[233]:


soup=BeautifulSoup(response.content)
soup


# In[235]:


title=[]
for i in soup.find_all('h2',class_="heading-6 flex items-center font-semi-bold m-0"):
    title.append(i.text)
print(title)


# In[236]:


location=[]
for i in soup.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95"):
    location.append(i.text)
print(location)


# In[238]:


area=[]
for i in soup.find_all('div',class_="font-semi-bold heading-6")[2::3]:
    area.append(i.text)
print(area)


# In[240]:


price=[]
for i in soup.find_all('div',class_="font-semi-bold heading-6")[::3]:
    price.append(i.text)
price


# In[242]:


emi=[]
for i in soup.find_all('div',class_="font-semi-bold heading-6")[1::3]:
    emi.append(i.text)
emi


# In[245]:


df=pd.DataFrame({"Title":title,"Location":location,"Area":area,"Price":price,"EMI":emi},index=range(1,len(title)+1))
df


# # Question 6

# In[246]:


url="https://www.bewakoof.com/bestseller?sort=popular%20."
response=requests.get(url)
response


# In[247]:


soup=BeautifulSoup(response.content)
soup


# In[253]:


prod_name=[]
for i in soup.find_all('div',class_="productNaming bkf-ellipsis"):
    prod_name.append(i.text.replace("Bewakoof®Women's ",""))
print(prod_name)


# In[258]:


prod_price=[]
for i in soup.find_all('div',class_="discountedPriceText"):
    prod_price.append(i.text)
print(prod_price)


# In[269]:


img=[]
for i in soup.find_all('img',class_="productImgTag"):
    img.append(i['src'])
img


# In[273]:


df=pd.DataFrame({"Product Name ":prod_name,"Product Price":prod_price,"Image Url":img},index=range(1,len(prod_name)+1))
df


# # QUESTION 7 

# In[319]:


url="https://www.cnbc.com/world/?region=world"
response=requests.get(url)
response


# In[320]:


soup=BeautifulSoup(response.content)
soup


# In[363]:


title=[]
for i in soup.find_all('div',class_="RiverHeadline-headline RiverHeadline-hasThumbnail")[:20]:
    title.append(i.text)
print(title)


# In[364]:


time=[]
for i in soup.find_all('span',class_="RiverByline-datePublished")[:20]:
    time.append(i.text)
time
    


# In[381]:


links=[div.a['href'] for div in soup.find_all('div',class_="RiverHeadline-headline RiverHeadline-hasThumbnail")[:]] 
l=[]
for link in links:
    l.append(link)
    
    for i in range(len(l)):
        if l[i]=="/pro/":
            l[i]="NA on site"
    print(l)
    


# In[382]:


df=pd.DataFrame({"Title":title,"Time":time,"Link":l})
df


# # Question 8

# In[4]:


url="https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/"


# In[5]:


response=requests.get(url)
response


# In[6]:


soup=BeautifulSoup(response.content)
soup


# In[7]:


title=[]
for i in soup.find_all('h2',class_="h5 article-title"):
    title.append(i.text.strip())
title


# In[8]:


date=[]
for i in soup.find_all('p',class_="article-date"):
    date.append(i.text)
date


# In[9]:


author=[]
for i in soup.find_all('p',class_="article-authors"):
    author.append(i.text)
author


# In[12]:


df=pd.DataFrame({"Title":title,"Date":date,"Author":author},index=range(1,len(title)+1))
df

