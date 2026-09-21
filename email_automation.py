'''
python -->Automation -->Email Automation -->Google Mail

Simple Mail automation
Mail OTP
Mail with Subject & Attachments
Bulk Mail

pkkn sukf cove zobp ;lakj
'''
#simple mail automation
#SMTP Simple mail transfer protocol
import smtplib
#first lets make srever connection
server = smtplib.SMTP('smto.gmail.com',587)
#print(server)
#start the connetion
server.starttls()
#login
server.login("kalyankorada16@gmail.com","fows xcve hgef ciyw")
msg = "hard work, discpaline ,consistency are need to reach success"
server.sendmail("kalyankorada16@gmail.com","sanjay43650@gmail.com",msg)
#close the connection
server.quit()
print("mail sent")

#Now let's send OTP to mail and validate the scripts

import math
import random
import smtplib
#in this case i will use math and random modules together 
digits = '123456789'
OTP = ""
for i in range(4):
    OTP += digits[math.floor(random.random()*10]
    #print(OTP)
msg = f'your OTP is {OTP}'
server = smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#Start the connetion
server.starttls()
#login
server.login("kalyankoradak

 
