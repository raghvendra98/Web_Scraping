# Web_Scraping
Web scraping using BS4
# gettting all link from wesite
all_link = set()
anchors = soup.find_all('a')
for link in anchors:
    if(link != '#'):
        link = "https://anysite.com" +link.get('href')
        all_link.add(link)
        print(link)
