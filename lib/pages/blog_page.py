from lib.base import PageBase, AssertionBase
from lib.pages.locators import JuloLandingBlogPageLocators

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class JuloLandingBlogPage(PageBase):
    def check_blog_page_is_open(self):
        self.logger.info("check if the blog page is opened")

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, JuloLandingBlogPageLocators.search_field)
            ),
            message='element {} not visible'.format(
                JuloLandingBlogPageLocators.search_field
            )
        )

    def get_list_of_navbar(self):
        self.logger.info('get list of navbar in blog page')

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, JuloLandingBlogPageLocators.navbar)
            ),
            message='element {} not visible'.format(
                JuloLandingBlogPageLocators.navbar
            )
        )

        list_of_navbar_element = self.driver.find_elements_by_xpath(
            JuloLandingBlogPageLocators.navbar
        )

        return ListOfNavbarAssertion(list_of_navbar_element)

    def click_download_button(self):
        self.logger.info('click navbar download button')
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, JuloLandingBlogPageLocators.download_button)
            ),
            message='element {} not visible'.format(
                JuloLandingBlogPageLocators.download_button
            )
        )

        navbar_download_element = self.driver.find_element_by_xpath(
            JuloLandingBlogPageLocators.download_button
        )
        navbar_download_element.click()


class ListOfNavbarAssertion(AssertionBase):
    def assert_success(self, expected_list):
        self.logger.info('assert list of navbar {}'.format(expected_list))
        for element in self.elements:
            assert element.text in expected_list, "{} is not in {}".format(
                element.text, expected_list
            )
