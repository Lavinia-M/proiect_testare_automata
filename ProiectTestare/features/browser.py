import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class Browser:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def close(self):
        self.driver.quit()

    def link_form_authentication(self):
        link_selector = (By.XPATH, '/html/body/div[2]/div/ul/li[21]/a')
        return self.driver.find_element(*link_selector)

    def get_current_url(self):
        return self.driver.current_url

    def link_add_remove_element(self):
        link_selector = (By.XPATH, '//*[@id="content"]/ul/li[2]/a')
        return self.driver.find_element(*link_selector)

    def link_file_download(self):
        link_file_download_selector = (By.XPATH, '//*[@id="content"]/ul/li[17]/a')
        return self.driver.find_element(*link_file_download_selector)

    def insert_invalid_username(self):
        invalid_username = self.driver.find_element(by=By.ID, value="username")
        return invalid_username.send_keys("popescu")

    def insert_invalid_password(self):
        invalid_pass = self.driver.find_element(by=By.ID, value="password")
        return invalid_pass.send_keys(1234)

    def login_button(self):
        login_btn_selector = self.driver.find_element(by=By.XPATH, value="//*[@id='login']/button")
        return login_btn_selector

    def error_message(self):
        error = self.driver.find_element(by=By.XPATH, value="//*[@id='flash']").text
        return error

    def message_secure_area(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "flash")))
        text_logged_secure_area = self.driver.find_element(by=By.XPATH, value="//*[@id='flash']")
        return text_logged_secure_area.text


