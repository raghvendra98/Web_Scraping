# Web_Scraping
Web scraping using BS4
# gettting all link from wesite
anchors = soup.find_all('a')
all_link = set()
#get all the link on the page
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" +link.get('href')
        all_link.add(link)
        print(linkText)
    
   
# comments
markup = "<p><!-- this is comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)

# .contents - A tag's children are available as a list (it would be fast)
# .children - A tag's children are available as a generator (store in momery)

# printing children, contents and string.
navbarSupportedContent = soup.find(id='navbarSupportedContent')
for elem in navbarSupportedContent.children:
    print(elem)

for elem in navbarSupportedContent.contents:
    print(elem)

for elem in navbarSupportedContent.strings:
    print(elem)

for elem in navbarSupportedContent.stripped_strings:
    print(elem)
    
# printing parrent
print(navbarSupportedContent.parent)

for item in navbarSupportedContent.parents:
    print(item)
    print(item.name)
    
print(navbarSupportedContent.next_sibling.next_sibling)
print(navbarSupportedContent.previous_sibling.previous_sibling)
    
