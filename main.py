import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"

r =requests.get(url)
htmlContent = r.content
#print(htmlContent)

soup =BeautifulSoup(htmlContent, "html.parser")
#print(soup.prettify)

title = soup.title
#print(type(soup))
#print(type(title))
#print(type(title.string))

paras = soup.find_all('p')
#print(paras)

#anchors = soup.find_all('a')
#all_link = set()
#get all the link on the page
#for link in anchors:
#    if(link.get('href') != '#'):
#        linkText = "https://codewithharry.com" +link.get('href')
#       all_link.add(link)
#        print(linkText)




#print(anchors)

#print((soup.find('p'))

#get class of any elements in html page
#print((soup.find('p'))['class'])

# find all the elements of the classess lead
#print(soup.find_all('p',class_="lead"))

#get the text from elements
#print(soup.find('p').get_text())

#print(soup.get_text())


#comments
markup = "<p><!-- this is comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)
