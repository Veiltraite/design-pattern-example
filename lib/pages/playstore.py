from lib.base import PageBase, AssertionBase
from lib.pages.locators import PlaystorePageLocators

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class PlaystorePage(PageBase):
    def check_playstore_page_is_opened(self):
        self.logger.info('check if julo playstore page is opened')
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, PlaystorePageLocators.playstore_logo)
            ),
            message='element {} not visible'.format(
                PlaystorePageLocators.playstore_logo
            )
        )

    def get_app_title(self):
        self.logger.info('get app title on playstore page')
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, PlaystorePageLocators.app_title)
            ),
            message='element {} not visible'.format(
                PlaystorePageLocators.app_title
            )
        )
        application_title_element = self.driver.find_element_by_xpath(
            PlaystorePageLocators.app_title
        )

        return AssertionAppTitle(application_title_element)

class AssertionAppTitle(AssertionBase):
    def assert_app_title(self, title):
        self.logger.info('assert app title {}'.format(title))
        assert self.elements.text == title, "title text is not {}".format(
            title
        )
