from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

#print(soup.prettify())

match = soup.title.text #give first title only
print(match)

match = soup.div
print(match)

match = soup.find('div')
print(match)

match = soup.find('div',class_= 'footer')
print(match)




