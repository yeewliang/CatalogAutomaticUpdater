#!/usr/bin/env python3
# Generate and send email

from email.message import EmailMessage
import mimetypes
import smtplib

def generate_email(sender, recipient, subject, body, report):
  # Crafting the email message
  message = EmailMessage()
  message["From"] = sender
  message["To"] = receipient
  message.set_content(body)
  message["Subject"] = subject
  attachment_filename = os.path.basename(report)
  mime_type, _ = mimetypes.guess_type(report)
  mime_type, mime_subtype = mime_type.split('/', 1)
  
  with open(report, 'rb') as ap:
    message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype,filename=os.path.basename(report))
  
  return message
    
def send_email(message):  
    # Sending the email through an smtp server
    mail_server = smtplib.SMTP("localhost")
    unsuccessful = mail_server.send_message(message)
    mail_server.quit()
    
    return unsuccessful