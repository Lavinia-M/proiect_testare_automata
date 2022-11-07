from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(BasePage):
    URL = "https://jules.app/sign-in"
    PAGE_TITLE = "Jules"
    PASSWORD_SELECTOR = (By.XPATH, "//input[@placeholder='Enter your password']")

    def go_to(self, url_text):
        element = self.driver.find_element(By.LINK_TEXT, url_text)
        element.click()

    def input_email(self, email):
        email_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[1]/div/div/input')
        email_element.send_keys(email)

    def input_password(self, password):
        password_element = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div/div[2]/div/div/input')
        password_element.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div/div[3]/button')
        login_button.click()

    def login_btn_enable(self):
        login_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div/div[3]/button')
        return login_button.is_enabled()

    def delete_password(self):
        password = self.driver.find_element(*SignInPage.PASSWORD_SELECTOR)
        password.send_keys(Keys.CONTROL + "a")
        password.send_keys(Keys.DELETE)

    def message_text_error(self):
        return self.driver.find_element(By.TAG_NAME, "p").text

    def sign_up_button(self):
        sign_up_button_selector = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div/div[4]/a')
        sign_up_button_selector.click()

    def password_text_visible(self):
        visible_txt_pass_selector = self.driver.find_element(By.XPATH,
                                                               '//input[@placeholder="Enter your password"]')
        visible_txt_pass_selector.click()




