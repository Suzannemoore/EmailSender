import smtpd
import smtplib
import ssl
from email.message import EmailMessage

subject = "How to send an email using python"
body = "Hello, this is your first email"
sender_email = "YOUR EMAIL"
receiver_email = "YOUR EMAIL"

password = input("Password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending message...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sender_email(sender_email, receiver_email, message.get_content)
print("Successfully sent")
