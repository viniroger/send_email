#!/usr/bin/env python3.9.7
# -*- coding: utf-8 -*-

import csv
import yagmail

# Define e-mail subject
subject = 'Visit our website'
# Define path/filename with names and e-mails
recipients = 'files/rec.csv'
# Define path/filename with body text
txt = open('files/msg.txt').read()
# Define attachment file name - list for more than one
att = 'files/att.pdf'
# Define logo image - leave empty if not using
logo_image = 'files/logo.png'

def send_mail(name, dest, subject, txt, att, logo_image):
    '''
    Mount and send e-mail
    '''
    yag = yagmail.SMTP({'YOUR_EMAIL@gmail.com': 'HAL9000'}, oauth2_file='credentials.json')
    #yag = yagmail.SMTP({'YOUR_EMAIL@gmail.com': 'SENDER NAME'}, password='YOUR_PASS')
    msg1 = f'Dear {name},\n\n{txt}\n\n'
    msg2 = f'Best regards,\n\
    HAL9000\n\
    Monolito Nimbus'
    # Adding image in the body of the email, after all text
    if logo_image:
        msg = [msg1, yagmail.inline(logo_image), msg2]
    else:
        msg = [msg1, msg2]
    #print(msg)
    #exit()
    # Send e-mail
    yag.send(to=dest, subject=subject, contents=msg, attachments=att)

# Read file with all e-mails (name,company,email)
with open(recipients, encoding='utf8') as fname:
    info = csv.DictReader(fname, dialect='excel')
    for row in info:
        name = row['name']
        dest = row['email']
        print(f'Sending mail to {name} - {dest}')
        send_mail(name, dest, subject, txt, att, logo_image)
        #exit()
