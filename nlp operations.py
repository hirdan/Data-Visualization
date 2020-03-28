import nltk
import bs4
import time
from urllib import request  #for downloading data from url
from bs4 import BeautifulSoup  #for souping
from nltk.tokenize import sent_tokenize,word_tokenize

#point to URL
url = 'https://en.wikipedia.org/wiki/Machine_learning'
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

web_data = mydata

sentences=sent_tokenize(web_data)

# print all sentences on by one

##for sent in sentences:
##    print(sent)
##    time.sleep(1)

#print(sentences)

#applying word tokenization
list_of_words=[]
for i in range(len(sentences)):
    list_of_words.append(word_tokenize(sentences[i]))

print(list_of_words)
