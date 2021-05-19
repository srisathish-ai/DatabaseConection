import time
import smtplib
from hdbcli import dbapi
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart

def checkConnection():
   try:
      conn = dbapi.connect(
         address="192.168.1.23",
         port=39017,
         user="system",
         password="passwd123"
      )
      return conn
   except Exception as e:
      return e

def mail():
   msse=MIMEText('HDC 192.168.1.23 - SAPHANA Conection failed')
   msse['Subject']='SAPHANA Connection failed'
   From = "from"
   msse['From'] = From
   toaddr = "to"
   msse['To']= toaddr
   s = smtplib.SMTP('smtp.office365.com', 587)
   s.starttls()
   s.login(From, "password")
   s.sendmail(From, toaddr, msse.as_string())
   s.quit()
   print("Mail sent Successfully")

if __name__ == '__main__':
   while True:
      data = checkConnection()
      try:
         if data.isconnected():
            print('SAPHANA connected successfully')
      except Exception as e:
         mail()
      time.sleep(300)
