#!/usr/bin/env python
# coding: utf-8

# Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# 
# Sample Text- 'Python Exercises, PHP exercises.'
# 
# Expected Output: Python:Exercises::PHP:exercises:
# 

# In[2]:


import re
sample_text="Pyhton Exercise,PHP exercises."
result=re.sub(',','::',sample_text)
result1=re.sub(' ',':',result)
result1


# Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
# 
# Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
# 
# Expected output-
# 
# 0      hello world
# 
# 1             test
# 
# 2    four five six
# 

# In[1]:


import numpy as np
import pandas as pd
import warnings 
warnings.filterwarnings('ignore')
Dictionary= {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df=pd.DataFrame(data=Dictionary)
df['SUMMARY']=df['SUMMARY'].str.replace('[^\w\s]|XXXXX','')
df


# Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

# In[4]:


text="I have four bananas in my bucket"
pattern=re.compile(r'\b\w{4,}\b')
result=pattern.findall(text)
print(result)


# Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

# In[5]:


text2="The brown dog ran so fast as lightning"
pattern=re.compile(r'\b\w{3,5}\b')
result=pattern.findall(text2)
result


# Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
# 
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# 
# Expected Output:
# 
#     example.com
# 
#     hr@fliprobo.com
# 
#     github.com
# 
#     Hello Data Science World
# 
#     Data Scientist
# 

# In[6]:


Sample_Text= ["example(.com)", "hr@fliprobo(.com)", "github(.com)", "Hello(Data Science World)", "Data(Scientist)"]

pattern=re.compile(r'\s*\(\s*|\s*\)\s*')

for text in Sample_Text:
    result=pattern.sub('',text)
    print(result)


# Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
# 
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# 
# Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
# 
# Note- Store given sample text in the text file and then to remove the parenthesis area from the text.
# 

# In[7]:


Sample_Text= ["example(.com)", "hr@fliprobo(.com)", "github(.com)", "Hello(Data Science World)", "Data(Scientist)"]

file=open("sample_text",'w')
for line in Sample_Text:
    file.write(line+"\n")
file.close()

file=open("sample_text",'r')
Sample_Text=file.readlines()

pattern = re.compile(r'\s*\(\s*|\s*\)\s*')

for text in Sample_Text:
    result=pattern.sub("",text.strip())
    print(result)
file.close()



# Question. Write a regular expression in Python to split a string into uppercase letters.
# 
# Sample text: “ImportanceOfRegularExpressionsInPython”
# 
# Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]
# 

# In[8]:


sample_text="ImportanceOfRegularExpressionsInPython"
pattern=re.compile(r'[A-Z][a-z]*')
result=pattern.findall(sample_text)
result


# Question 8- Create a function in python to insert spaces between words starting with numbers.
# 
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# 
# Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython
# 

# In[9]:


def insert_spaces(text):
    return re.sub(r'(\d)([A-Za-z])',r' \1\2',text)
SampleText="RegularExpression1IsAn2ImportantTopic3InPython"
result=insert_spaces(SampleText)
print(result)


# Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
# 
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# 
# Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython
# 

# In[10]:


def insert_spaces(text):
    return re.sub(r'(\d)([A-Za-z])',r' \1 \2',text)
SampleText="RegularExpression1IsAn2ImportantTopic3InPython"
result=insert_spaces(SampleText)
print(result)


# Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.

# In[16]:


url='https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv'
df=pd.read_csv(url)
df['Five_Letter']=df['Country'].str[:6]
print(df.head())
print(df['Five_Letter'])


# Question11. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[17]:


import re

x=input("Enter a string : ")
pattern=r'^[a-zA-Z0-9_]+$'

if re.match(pattern,x):
    print("This string contains uppercase , lowercase ,numbers and underscore only")
else:
    print("Pattern isn't matching :( ")


# Question 12- Write a Python program where a string will start with a specific number. 

# In[24]:


string=input("Enter the string : ")
specific_number=input("Enter the specific number the string should start from : ")

if string.startswith(specific_number):
    print("The string starts with specific_number ",specific_number)
else:
    print("The string isnt starting from specific numnber ",specific_number)


# Question 13 - Write a Python program to remove leading zeros from an IP address

# In[4]:


ipaddress=input("Enter IP address : ")
parts=ipaddress.split('.')
x=[str(int(part))for part in parts]
result='.'.join(x)
print("Cleaned IP : ",result)


# Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
# 
# Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
# 
# Expected Output- August 15th 1947
# Note- Store given sample text in the text file and then extract the date string asked format.
# 

# In[18]:


import re
Sample_text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country"
file=open('Sample_text.txt','r')
text=file.read()
print("Text from file : ",text)
file.close()
pattern=r'[A-Z][a-z]+\s\d{1,2}(?:st|nd|rd|th)\s\d{4}'
matches=re.findall(pattern,text)
for match in matches:
    print(match)


# Question 15 : Write a Python program to search some literals strings in a string. 
# 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# 
# Searched words : 'fox', 'dog', 'horse'
# 

# In[23]:


Sample_text="The quick brown fox jumps over the lazy dog "
searched_words=['fox','dog','horse']
for words in searched_words:
    if words in Sample_text:
        print(words," : found in the sample text :)")
    else:
        print(words, " : Match not found :( ")


# Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# 
# Searched words : 'fox'
# 

# In[5]:


Sample_text="The quick brown fox jumps over the lazy dog"
searched_word='fox'
location=Sample_text.find(searched_word)
if location != -1:
    print(searched_word , " Exists! Match found")
else:
    print(searched_word," 404! Not found")


# Question 17- Write a Python program to find the substrings within a string.
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern : 'exercises'.
# 

# In[3]:


Sample_text="Python exercises , PHP exercises , C# exercises "
print("Sample_text= Python exercises , PHP exercises , C# exercises ")
Pattern="exercises"
print("Pattern=exercises")
if Pattern in Sample_text:
    print("Pattern Match")
else:
    print("Not Found !!")


# Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

# In[2]:


import re
string=input("Enter the main string : ")
substring=input("Enter the substring to search for : ")

if substring in string:
    print("Substring found at position(s)",[i for i in range(len(string)) if string.startswith(substring,i)])
    print("Total occurrences : ",string.count(substring))
else:
    print("Substring not found in the given string.")


# Question 19 - Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[5]:


date=input("Enter a date in yyyy-mm-dd : ")
year,month,day=date.split("-")
result_date=print("Converted date -",day,"-",month,"-",year)


# Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
# 
# Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
# 
# Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']
# 

# In[6]:


import re
sample_text= "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
pattern=re.compile(r'\b\d+\.\d{1,2}\b')
decimalnum=pattern.findall(sample_text)
print(decimalnum)


# Question 21- Write a Python program to separate and print the numbers and their position of a given string.

# In[11]:


string=input("Enter the string : ")
print("Number found in the string : ")
for i in range(len(string)):
    if string[i].isdigit():
        print("number : ",string[i],"Position : " ,[i])


# Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
# 
# Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
# 
# Expected Output: 950
# 

# In[13]:


sampletext='My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
max_value=max(map(int,re.findall(r'\d+',sampletext)))
print("max num value :",max_value)


# Question 23- Create a function in python to insert spaces between words starting with capital letters.
# Sample Text: “RegularExpressionIsAnImportantTopicInPython"
# Expected Output: Regular Expression Is An Important Topic In Python
# 

# In[18]:


sample_text = "RegularExpressionIsAnImportantTopicInPython"
result=re.sub(r'([A-Z])',r' \1',sample_text)
print(result)


# Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

# In[19]:


sampletext="This Is A Sample Text With Multiple Sequences of Uppercase And Lowercase Letter"
pattern=r'[A-Z][a-z]+'
result=re.findall(pattern,sampletext)
print(result)


# Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
# 
# Sample Text: "Hello hello world world"
# 
# Expected Output: Hello hello world
# 

# In[21]:


sampletext="Hello hello world world"
pattern=r'\b(\w+)( \1\b)+'
result=re.sub(pattern,r' \1',sampletext)
print(result)


# Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

# In[25]:


string=input("Enter the string : ")
if re.search(r'\w$',string):
    print("Input string ends with an alphanumeric character")
else:
    print("Input string does not end with an alphanumeric character")


# Question 27-Write a python program using RegEx to extract the hashtags.
# 
# Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
# 
#    Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']
# 

# In[26]:


sampletext="""RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
pattern=r'#\w+'
result=re.findall(pattern,sampletext)
print(result)


# Question 28- Write a python program using RegEx to remove <U+..> like symbols
# Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
# 
# Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
# 
# Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders
# 

# In[28]:


sampletext="@Jags123456 Bharat band on 28??<U+00A0><U+00BD><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"
pattern=r'<U\+\w{4}>'
result=re.sub(pattern,'',sampletext)
print(result)


# Question 29- Write a python program to extract dates from the text stored in the text file.
# 
# Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
# 
# Note- Store this sample text in the file and then extract dates.
# 

# In[30]:


file=open('sampletext1.txt','r')
text=file.read()
file.close()
dates=re.findall(r'\d{2}-\d{2}-\d{4}',text)
print(dates)


# Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
# The use of the re.compile() method is mandatory.
# 
# Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# 
# Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.
# 

# In[31]:


sampletext="The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
pattern=re.compile(r'\b\w{2,4}\b')
result=pattern.sub('',sampletext)
print(result)

