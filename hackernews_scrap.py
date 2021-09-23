import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# system date and time manipulation
import datetime
now = datetime.datetime.now()

content = ''

# extracting hacker news stories


def extract_news(url):
    print("extracting news from hacker news........")
    cnt = ' '
    cnt += ('<b> HN Top Stories : </b>\n'+'<br>'+'-'*50 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td', attrs={'class': 'title','valign': ''})):
        cnt += ((str(i+1) + "::" + tag.text + "\n" + '<br>') if tag.text != 'More' else '')

    return(cnt)


cnt = extract_news("https://news.ycombinator.com/")
content += cnt
content += ('<br>.........<br>')
content += ('<br><br>End of Message')
print(content)

# lets send the email again
print("composing email......")

# update your email details
SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'yogeshjbhati1996@gmail.com'
TO = 'yogeshjbhati1996@gmail.com'
PASS = "Bhati@786"

msg = MIMEMultipart()
msg['Subject'] = "top news stories from hacker news" + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content , "html"))

print("intialising server .....")

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()

server.login(FROM, PASS)
server.sendmail(FROM,TO, msg.as_string())

print("Email sent....")

server.quit()


