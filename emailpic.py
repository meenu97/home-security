#!/usr/bin/env python
import smtplib,os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def mail(name):
 fromaddr = "sherlock.techsavvy@gmail.com"
 toaddr = "sivalapuri@gmail.com"
 ccaddr = "Magictaurus12@gmail.com"
 bccaddr = "sherlock.techsavvy@gmail.com"
 alladdr = toaddr.split(",") + ccaddr.split(",") + [bccaddr]

 msg = MIMEMultipart()

 msg['From'] = fromaddr
 msg['To'] = toaddr
 msg['Subject'] = "Some one's home"
 body = "Hello check out the attachment. "+name+" has come home"
 msg.attach(MIMEText(body, 'plain'))
 path2 = '/home/pi/detectedfaces'
 image_paths = [os.path.join(path2, f) for f in os.listdir(path2)]
 for image_path in image_paths:
      filename = os.path.basename(image_path)
      attachment = open(image_path, "rb")
      part = MIMEBase('application', 'octet-stream')
      part.set_payload((attachment).read())
      encoders.encode_base64(part)
      part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
      msg.attach(part)
 
 print("mailing")
 server = smtplib.SMTP('smtp.gmail.com', 587)
 server.starttls()
 server.login(fromaddr, "holmes123")
 text = msg.as_string()
 server.sendmail(fromaddr, alladdr, text)
 server.quit()

