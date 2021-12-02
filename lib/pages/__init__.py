def get_julo_landing_homepage(driver):
    from .homepage import JuloLandingHomepage
    return JuloLandingHomepage(driver)

def get_julo_landing_blog_page(driver):
    from .blog_page import JuloLandingBlogPage
    return JuloLandingBlogPage(driver)

def get_playstore_page(driver):
    from .playstore import PlaystorePage
    return PlaystorePage(driver)
