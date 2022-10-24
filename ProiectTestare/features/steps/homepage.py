from behave import *
from time import sleep


@given("I am on the home page")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/")


@when("I click the Form Authentication link")
def step_impl(context):
    link = context.browser.link_form_authentication()
    link.click()


@then("I am redirected to the Form Authentication page")
def step_impl(context):
    expected_url = "https://the-internet.herokuapp.com/login"
    assert context.browser.get_current_url() == expected_url


sleep(2)


@when("I click the Add Remove Elements link")
def step_impl(context):
    link = context.browser.link_add_remove_element()
    link.click()


@then("I am redirected to the Add Remove Elements page")
def step_impl(context):
    expected_url = "https://the-internet.herokuapp.com/add_remove_elements/"
    assert context.browser.get_current_url() == expected_url


sleep(2)


@when("I click the File Download link")
def step_impl(context):
    link = context.browser.link_file_download()
    link.click()


@then("I am redirected to the File Download page")
def step_impl(context):
    expected_url = "https://the-internet.herokuapp.com/download"
    assert context.browser.get_current_url() == expected_url


sleep(2)
