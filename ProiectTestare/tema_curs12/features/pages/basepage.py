
class BasePage:

    URL = ''
    PAGE_TITLE = ''

    def __init__(self, driver):
        self.driver = driver

    def go_home(self):
        self.driver.get(self.URL)

    def verify_url(self):
        assert self.driver.get_current_url == self.URL

    def get_current_url(self):
        return self.driver.current_url

