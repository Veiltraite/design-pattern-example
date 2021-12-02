from lib.base import PageBase, AssertionBase
from lib.pages.locators import JuloLandingHomepageLocators

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class JuloLandingHomepage(PageBase):
    def check_homepage_is_open(self):
        self.logger.info("check if the homepage is opened")
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, JuloLandingHomepageLocators.julo_logo)
            ),
            message='element {} not visible'.format(
                JuloLandingHomepageLocators.julo_logo
            )
        )

    def get_list_of_navbar(self):
        self.logger.info('get list of navbar in homepage')

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, JuloLandingHomepageLocators.navbar)
            ),
            message='element {} not visible'.format(
                JuloLandingHomepageLocators.navbar
            )
        )

        list_of_navbar_element = self.driver.find_elements_by_xpath(
            JuloLandingHomepageLocators.navbar
        )

        return ListOfNavbarAssertion(list_of_navbar_element)

    def click_navbar_blog_button(self):
        self.logger.info('click navbar blog button')

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, JuloLandingHomepageLocators.blog_button)
            ),
            message='element {} not visible'.format(
                JuloLandingHomepageLocators.blog_button
            )
        )

        navbar_blog_element = self.driver.find_element_by_xpath(
            JuloLandingHomepageLocators.blog_button
        )
        navbar_blog_element.click()


class ListOfNavbarAssertion(AssertionBase):
    def assert_success(self, expected_list):
        self.logger.info('assert list of navbar {}'.format(expected_list))
        for element in self.elements:
            assert element.text in expected_list, "{} is not in {}".format(
                element.text, expected_list
            )
