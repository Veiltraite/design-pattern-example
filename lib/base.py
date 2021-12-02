import logging
from selenium.webdriver.support.ui import WebDriverWait

class AssertionBase():
    def __init__(self, elements):
        self.logger = logging.getLogger(__name__)
        self.elements = elements

class PageBase():
    def __init__(self, driver):
        self.logger = logging.getLogger(__name__)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
