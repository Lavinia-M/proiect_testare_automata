# from behave import *
# from time import sleep
#
#
# @given("I am on the login page")
# def step_impl(context):
#     context.browser.driver.get("https://the-internet.herokuapp.com/login")
#
#
# @when("I enter username ")
# def step_impl(context):
#     context.browser.insert_invalid_username()
#
#
# sleep(1)
#
#
# @when("I enter password ")
# def step_impl(context):
#     context.browser.insert_invalid_password()
#
#
# sleep(1)
#
#
# @when("I press the login button")
# def step_impl(context):
#     login_click = context.browser.login_button()
#     login_click.click()
#
#
# sleep(1)
#
#
# @then("I receive an error message")
# def step_impl(context):
#     expected = "Your username is invalid!"
#     assert context.browser.error_message() == expected
#
#
# sleep(1)
