from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
import time


class CouncilProcess:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def run(self):
        self.driver.get(self.url)

        image = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.XPATH, value='//*[@alt="Необходимо включить загрузку картинок в браузере."]'))

        print(image.screenshot_as_base64)

        time.sleep(5)
