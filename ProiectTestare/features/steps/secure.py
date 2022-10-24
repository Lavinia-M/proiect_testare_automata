from behave import *
from time import sleep


@given("I am on the secure page")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/secure")


@then("I receive a confirmation message")
def step_impl(context):
    expected = "You logged into a secure area!"
    assert context.browser.message_secure_area() == expected

sleep(2)

