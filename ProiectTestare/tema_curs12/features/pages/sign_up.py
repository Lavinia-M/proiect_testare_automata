from pages.basepage import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SignUpPage(BasePage):
    URL = "https://jules.app/sign-up"
    PAGE_TITLE = "Jules"

    def go_to(self, url_text):
        element = self.driver.find_element(By.LINK_TEXT, url_text)
        element.click()

    def go_to_login_btn(self):
        login_btn_selector = self.driver.find_element(By.XPATH, '//*[@href="/sign-in"]')
        login_btn_selector.click()

    def person_button(self):
        selector_button = (By.XPATH, "//input[@value='personal']")
        self.driver.find_element(selector_button).click()

    def continue_button(self):
        selector_continue_btn = self.driver.find_element(By.XPATH, "//span[contains(text(),'CONTINUE')]")
        selector_continue_btn.click()

    def input_field(self, field):
        field_element = self.driver.find_element(By.XPATH, "//input[@placeholder='Type your answer here...']")
        field_element.send_keys(field)

    def message_error_displayed(self):
        warning_message_selector = (By.XPATH, "//p[contains(text(),'Please enter a valid email address.')]")
        try:
            displayed = self.driver.find_element(*warning_message_selector).is_displayed()
        except NoSuchElementException as e:
            displayed = False

        if displayed:
            text = self.driver.find_element(*warning_message_selector).text
        else:
            text = "NoSuchElement"
        return displayed, text

