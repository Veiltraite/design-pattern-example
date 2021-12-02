from lib.drivers import get_chrome_driver
from lib.pages import (
    get_julo_landing_homepage
)
import pytest

@pytest.fixture
def driver():
    return get_chrome_driver()

def test_navbar_on_homepage(driver):
    julo_landing_homepage = get_julo_landing_homepage(driver)
    julo_landing_homepage.open()
    list_of_navbar = julo_landing_homepage.get_list_of_navbar()
    list_of_navbar.assert_success(
        ['Home','Produk','Blog','Tentang','FAQ']
    )
