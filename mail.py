#!/usr/bin/env python3
'''Mail service'''
import smtplib
import ssl
# import getpass

SMTP_SERVER = "smtp.gmail.com"
PORT = 465  # For SSL
PASSWORD = 'ebks pxnu iopz qevj'
# Create a secure SSL context
CONTEXT = ssl.create_default_context()
SENDER_EMAIL = "abdofola67@gmail.com"
RECEIVER_EMAIL = "abdallah_alkaser@outlook.com"
MESSAGE = """\
Subject: Hi there

This message is sent from Python."""

with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=CONTEXT) as server:
    server.login(SENDER_EMAIL, PASSWORD)
    # Send email here
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, MESSAGE)
