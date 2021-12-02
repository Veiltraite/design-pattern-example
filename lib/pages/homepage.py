from lib.pages.base import PageSetting
from lib.pages.locators import JuloLandingHomepageLocators

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class JuloLandingHomepage(PageSetting):
    def open(self):
        login_url = 'https://www.julo.co.id/'

        self.logger.info('open {}'.format(login_url))
        self.driver.get(login_url)

        self.wait.until(
        EC.visibility_of_element_located(
                (By.XPATH, JuloLandingHomepageLocators.julo_logo)
            )
        )
        self.logger.info('success')

    def get_list_of_navbar(self):
        self.logger.info('get list of navbar in homepage')

        self.wait.until(
        EC.visibility_of_element_located(
                (By.XPATH, JuloLandingHomepageLocators.navbar)
            )
        )

        list_of_navbar_element = self.driver.find_elements_by_xpath(
            JuloLandingHomepageLocators.navbar
        )

        return ListOfNavbarAssertion(list_of_navbar_element)
        self.logger.info('success')


class ListOfNavbarAssertion():
    def __init__(self, elements):
        self.elements = elements

    def assert_success(self, expected_list):
        for element in self.elements:
            assert element.text in expected_list, "{} is not in {}".format(
                element.text, expected_list
            )
