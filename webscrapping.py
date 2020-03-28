import nltk
import bs4
import time
import re # importing regular expression
from urllib import request  #for downloading data from url
from bs4 import BeautifulSoup  #for souping
from nltk.corpus import stopwords

#point to URL
#url = 'https://en.wikipedia.org/wiki/Machine_learning'
#url = 'https://www.who.int/data/gho/info/gho-odata-api'
url = 'https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic'
htmldata=request.urlopen(url)

#htmldata.read() # it will download data in html format.

soupdata = BeautifulSoup(htmldata,'html5lib')
#html data, html parser

#html parser-collection of html tags that can scrape data from particular tag like h1, html, a ,p.


# now selecting a particular tag for data scrape
ptagdata = soupdata.findAll('p')
#print(ptagdata)

# now converting data into string format from HTML format
mydata=''
for i in ptagdata:
    mydata += i.text
    #print(i.text)
    #time.sleep(1)
#print(mydata)    

#  dATA cleaning
clean_data=re.sub(r'\[[0-9]*\]',' ',mydata)  #  this will remove 0 or more times number appearing in mydata
clean_data=re.sub(r'\s+',' ',clean_data)  # it will remove one or more white spaces with single white space
clean_data=re.sub(r'[^a-zA-Z]',' ',clean_data)  # it will remove single char from starting of the line
clean_data=re.sub(r'\s+',' ',clean_data)  # it will remove one or more white spaces with single white space
#print(clean_data)
#print(type(clean_data))

# now lets deal with strings
newdata=clean_data.split()   #conversion of string to list
##for words in newdata:
##    print(words)
    #time.sleep(1)

# deal with data by using NLTK----natural language toolkit
#first removing stopwords
mypuredata=[]
for i in newdata:
    if i.lower() not in stopwords.words('english'):
        mypuredata.append(i)
print(mypuredata)        
freq_data = nltk.FreqDist(mypuredata)
freq_data.plot(20) #top 20 words having the most count
