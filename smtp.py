import smtplib, ssl, os


"""
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "my@gmail.com"  # Enter your address
receiver_email = "your@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")"""
"""
message = ""\
Subject: Hi there

This message is sent from Python.""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    """

def message_send(message):
    port = 465  # For SSL

    smtp_server = "smtp.gmail.com"
    sender_email = 'devopsesi2022@gmail.com'
    receiver_email = 'devopsesi2022@gmail.com'
    password = 'unkj vlla dtat dxkd'  # os.getenv

    # Message = f""" \
    # Subject: Hi
    #
    #
    #
    #{message} . """
    # Create a secure SSL context
    context = ssl.create_default_context()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

#send_message()