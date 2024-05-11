import smtplib
from email.message import EmailMessage
import os

def email_alert(subject, body, to, attachment_folder=None):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "testing123456qaz@gmail.com"  # Email address from which you want to send
    msg['from'] = user
    password = "xrkpfwpwqjjgiuyn"  # App_password

    if attachment_folder:
        for filename in os.listdir(attachment_folder):
            filepath = os.path.join(attachment_folder, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'rb') as f:
                    file_data = f.read()
                    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=filename)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

def send_email(to):
    subject = "Processed Text Files"
    body = "Find the attachments"
    attachment_folder = "classified_text"
    email_alert(subject, body, to, attachment_folder)

# if __name__ == '__main__':
#     recipient_email = input("Enter recipient's email address: ")
#     send_email(recipient_email)
