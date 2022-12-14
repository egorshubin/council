from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Email import Email
from AnticaptchaApi import AnticaptchaApi
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Db import Db
import os
from dotenv import load_dotenv

_ = load_dotenv()


class CouncilProcess:
    def __init__(self, url):
        self.url = url

        chrome_options = Options()
        chrome_options.set_capability('unhandledPromptBehavior', 'accept')
        self.driver = webdriver.Chrome(options=chrome_options)

    def run(self):
        self.driver.get(self.url)

        image = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.XPATH,
                                                                                      value='//*[@alt="Необходимо включить загрузку картинок в браузере."]'))

        anticap = AnticaptchaApi(image.screenshot_as_base64)
        captcha_text = anticap.solve()

        result = self.walk_on_site(captcha_text)

        message = str(result) + ' ' + str(self.url)

        Db(int(bool(result)), self.url).log()

        if captcha_text:
            self.send(result, message)

    def send(self, result, message):
        if bool(int(os.environ.get("TEST_MODE"))):
            email = Email(str(result))
            email.send()
        elif result != 0:
            email = Email(message)
            email.send()
        else:
            print('No email')

    def walk_on_site(self, captcha_text):
        input_code = self.driver.find_element(by=By.ID, value="ctl00_MainContent_txtCode")
        input_code.send_keys(captcha_text)
        input_code.send_keys(Keys.RETURN)

        if self.captcha_error_exists():
            return 0

        submit1 = self.driver.find_element(by=By.CLASS_NAME, value="btn")
        submit1.click()

        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
        except:
            print('Alert check passed')

        calendar = WebDriverWait(self.driver, timeout=10).until(
            lambda d: d.find_element(by=By.ID, value='ctl00_MainContent_Calendar'))

        if calendar.get_attribute('disabled'):
            return 0

        main = WebDriverWait(self.driver, timeout=10).until(
            lambda d: d.find_element(by=By.ID, value='center-panel'))

        labels = main.find_elements(by=By.TAG_NAME, value='label')

        txt_labels = []
        for element in labels:
            txt_labels.append(element.text)

        return ' / '.join(txt_labels)

    def captcha_error_exists(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(by=By.ID, value='ctl00_MainContent_lblCodeErr'))
        except:
            return False
        return True
