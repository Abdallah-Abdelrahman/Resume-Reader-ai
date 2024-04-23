#!/usr/bin/env python3
'''Mail service'''
import smtplib
import ssl
import getpass

SMTP_SERVER = "smtp.gmail.com"
PORT = 465  # For SSL
PASSWORD = 'ebks pxnu iopz qevj'
# Create a secure SSL context
CONTEXT = ssl.create_default_context()
SENDER_EMAIL = "abdofola67@gmail.com"
RECEIVER_EMAIL = "mohannadabdo21@gmail.com"
MESSAGE = """\
Subject: Hi there

This message is sent from Python."""

'''
# Try to log in to server and send email
try:
    server = smtplib.SMTP(SMTP_SERVER, PORT)
    server.ehlo()  # Can be omitted
    server.starttls(context=CONTEXT)  # Secure the connection
    server.ehlo()  # Can be omitted
    server.login(SENDER_EMAIL, PASSWORD)
    # Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()

'''
with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=CONTEXT) as server:
    server.login(SENDER_EMAIL, PASSWORD)
    # Send email here
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, MESSAGE)
