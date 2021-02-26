import requests
from bs4 import BeautifulSoup
import subprocess
import time
import smtplib
import  os

# def send_mail(msg):
#     email = os.environ.get("hbraghvendra@gmail.com")
#     password = os.environ.get("HB@2021#")
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls()
#     s.login(email, password)
#     s.sendmail(email, "hbraghvendra@gmail.com", msg)
#     s.sendmail(email, ".com", msg)
#     s.quit()
#     print (msg)
#     print("Sent")

# def send(msg):
#     subprocess.Popen(['notify-send', msg])
#     return
def send_mail_to_me():
    sen_email = "@gmail.com"
    rec_email = ".in"
    password = ""
    msg = """From: From Person <from@hbraghvendra@gmail.com>
To: To Person <to@hbraghvendra@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Ticket is available

<b>Ticket is Available for 1ST T20 match between <h3>IND and ENG</h3></b>

<html>
<body>
       <p><h1><a href="https://in.bookmyshow.com/explore/sports/">Book here</a></h1></p>
</body>
</html>


"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sen_email, password)
    print("login success")
    server.sendmail(sen_email, rec_email, msg)
    print("email has beeen sent to", rec_email)
    server.quit()

url = "https://in.bookmyshow.com/explore/sports"

r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, "html.parser")


var = soup.find('body').find_all('img')
for i in var:
    if i["alt"] == "4th Test India vs England" or i["alt"] == "1st T20 India vs England":
        #print("msg sending")
        send_mail_to_me()
        # send_mail(msg=" T20 tickets are available")
        # send(" tickets are available")
        break
    else:
        continue
else:
    print("Ticket not available yet")

# if var == "4th Test India vs England":
#     print("yes")
# else:
#     print("no")


# (soup.get('alt')):





#if req_line == "1st T20 India vs England" or req_line == "4th Test India vs England":
#    print("found")
#else:
#    print("server Fail")

