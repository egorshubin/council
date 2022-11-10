import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

_ = load_dotenv()


class Email:
    def __init__(self, url):
        self.email_from = os.environ.get("EMAIL_FROM")
        self.app_password = os.environ.get("APP_PASSWORD")
        self.email_to = os.environ.get("EMAIL_TO")
        self.url = url

    def send(self):
        try:
            if self.email_from is None or self.app_password is None:
                print("Did you set email-from and password correctly?")
                return False

            # create email
            msg = EmailMessage()
            msg['Subject'] = 'Successful council'
            msg['From'] = self.email_from
            msg['To'] = self.email_to
            msg.set_content(self.url)

            # send email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email_from, self.app_password)
                smtp.send_message(msg)
            return True
        except Exception as e:
            print("Problem during send email")
            print(str(e))
        return False
