import logging
from selenium.webdriver.support.ui import WebDriverWait

class PageSetting():
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 10)
