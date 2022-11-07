from browser import Browser
from pages.basepage import BasePage
from pages.sign_in import SignInPage
# from pages.sign_up import SignUpPage


def before_all(context):
    print('Setting the browser!')
    context.browser = Browser()
    context.sign_in = SignInPage(context.browser.driver)
    # context.sign_up = SignUpPage(context.browser.driver)


def after_all(context):
    context.browser.close()

