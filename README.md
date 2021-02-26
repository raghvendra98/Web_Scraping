# Web_Scraping
Web scraping using BS4

using BS4 Write a code that for BookMyShow site for Checking Ticket availability 
ie: If ticket would be available will be available for selling i will get a maessage to my email id that "Tickets are Available"
(example - if tickets will be available for selling for IND VS ENG for 1st test match i will get auto message to my email ID.)


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
    


# SENDING MESSAGE TO EMAIL ID
    sen_email = "youremailid@gmail.com"
    rec_email = "senderemailid@gmail.com"
    password = "youremailidpassword#"
    msg = "message you want to send"
    server = smtplib.SMTP('smtp.gmail.com', 587)//server login
    server.starttls()
    server.login(sen_email, password)your acc login to server
    print("login success") 
    server.sendmail(sen_email, rec_email, msg)
    print("email has beeen sent to", rec_email)
    server.quit()
