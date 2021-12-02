from lib.drivers import get_chrome_driver
from lib.pages import (
    get_julo_landing_homepage,
    get_julo_landing_blog_page
)
import pytest

@pytest.fixture
def driver():
    return get_chrome_driver()

def test_navbar_on_homepage(driver):
    driver.get('https://www.julo.co.id/')

    julo_landing_homepage = get_julo_landing_homepage(driver)
    julo_landing_homepage.check_homepage_is_open()
    list_of_navbar = julo_landing_homepage.get_list_of_navbar()
    list_of_navbar.assert_success(
        ['Home','Produk','Blog','Tentang','FAQ']
    )

    driver.quit()

def test_navbar_on_blog_page(driver):
    driver.get('https://www.julo.co.id/')

    julo_landing_homepage = get_julo_landing_homepage(driver)
    julo_landing_homepage.click_navbar_blog_button()

    julo_landing_blog_page = get_julo_landing_blog_page(driver)
    julo_landing_blog_page.check_blog_page_is_open()
    list_of_navbar = julo_landing_blog_page.get_list_of_navbar()
    list_of_navbar.assert_success(
        ['Beranda','Promo','Tips Keuangan','Gaya Hidup',
        'Karir & Pendidikan', 'Press Release', 'Tentang', 'Download']
    )

    driver.quit()
