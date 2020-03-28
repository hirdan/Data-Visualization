#importing modules

from bs4 import BeautifulSoup # web scrapping
import requests    # replacement of URLLIB
import time # to give some delay message
import csv

# now talking corona live data set
url='https://www.worldometers.info/coronavirus/'

#now connecting with https protocol
htmlpage = requests.get(url)

#print info
#print(htmlpage.content)

purehtmlpage = htmlpage.content
soup = BeautifulSoup(purehtmlpage,'html5lib') #souping

#to check type
#print(type(soup))

tb=soup.find_all('table', class_="table table-bordered table-hover main_table_countries")
file = open('corona.csv','w')
#finding all table rows

for trr in tb[0].find_all('tr'):
    for rows in trr.find_all('th'):
        tableheading = rows.text
        print(tableheading)
        file.write(tableheading)          

# now scrapping data for each row with normal country data

for trr1 in tb[0].find_all('tr'):
    for rows in trr1.find_all('td'):
        tabledata = rows.text
        print(tabledata)
        file.write(tabledata)

file.close()


