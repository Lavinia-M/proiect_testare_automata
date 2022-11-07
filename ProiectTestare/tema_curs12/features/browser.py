from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Browser:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver.get("https://jules.app/sign-in")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        sleep(5)

    def close(self):
        self.driver.quit()


