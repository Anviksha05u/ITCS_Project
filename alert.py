import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from enail.mime.image import MIMEImage
from enail.mime.base import MIMEBase
import configure 
def msg():
  subject="ALERT!"
  msg=MIMEMultipart()
  msg['From']=configure.USER_NAME
  msg['To']=configure.USER_NAME
  msg['Subject']=subject
  body="Activity Detected"
  msg.attach(MIMEText(body))
  fp=open("screen5.pnhg")
  img=MIMEImage(fp.read())
  fp.close()
  s=smptlib.
