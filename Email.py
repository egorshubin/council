import os
from dotenv import load_dotenv
_ = load_dotenv()

class Email:
    def __init__(self, url):
        self.email_from = os.environ.get("EMAIL_FROM")
        self.app_password = os.environ.get("APP_PASSWORD")
        self.email_to = os.environ.get("EMAIL_TO")
        self.url = url

