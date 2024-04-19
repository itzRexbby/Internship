#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[ ]:


#QUESTION 1
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[4]:


url='https://en.wikipedia.org/wiki/Main_Page'
response=requests.get(url)
response


# Page Content

# In[6]:


soup=BeautifulSoup(response.content)
soup


# In[8]:


#For Header Tags
header_tag=[]
for i in soup.find_all('span',class_="mw-headline"):
    header_tag.append(i.text)
header_tag


# # Question 2 

# In[29]:


#Question 2
url='https://www.imdb.com/list/ls091520106/'
response=requests.get(url)
response


# In[30]:


soup=BeautifulSoup(response.content)
soup


# In[31]:


names=[]
for i in soup.find_all('h3',class_="lister-item-header"):
    names.append(i.text.strip().replace('\n',' '))
names


# In[32]:


rating=[]
for i in soup.find_all('span',class_="ipl-rating-star__rating")[::23]:
    rating.append(i.text.strip())
rating


# In[34]:


df=pd.DataFrame({"Name & Year of release":names,"Rating":rating})
df


# # Question 3

# In[43]:


#Question 3
url='https://www.dineout.co.in/delhi-restaurants/buffet-special'
response=requests.get(url)
response


# In[44]:


soup=BeautifulSoup(response.content)
soup


# In[45]:


titles=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
    titles.append(i.text)
titles


# In[46]:


location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
location


# In[51]:


price=[]
for i in soup.find_all('span',class_="double-line-ellipsis"):
    price.append(i.text.replace('₹',' '))
price


# In[52]:


images=[]
for i in soup.find_all('img',class_="no-img"):
    images.append(i['data-src'])
images


# In[53]:


rating=[]
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)
rating


# In[57]:


df=pd.DataFrame({"Restaurant_name":titles,"Location":location,"Rating":rating,"Price | Cuisine":price,"Image_URL":images})
df


# # Question 4  On site tenture are'nt present

# In[52]:


#Question 4
url='https://presidentofindia.nic.in/former-presidents'
response=requests.get(url)
response


# In[53]:


soup=BeautifulSoup(response.content)
soup


# In[54]:


names=[]
for i in soup.find_all('div',class_="desc-sec"):
    names.append(i.text.strip().replace('\n'," : ").split(' : '))
names
df=pd.DataFrame(data=names,columns=["Name","Order"])
df


# In[ ]:




