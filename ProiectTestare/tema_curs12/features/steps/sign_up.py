from behave import *
from time import sleep


@Given('I am on the Jules SignIn page')
def step_impl(context):
    context.sign_in.go_home()


@When('I click sign up button')
def step_impl(context):
    context.sign_in.sign_up_button()
    sleep(2)


@Then('I am redirected on the Sign up page')
def step_impl(context):
    sleep(2)
    assert context.sign_up.get_current_url() == context.sign_up.URL
    sleep(2)


@Then('I click login button')
def step_impl(context):
    context.sign_up.go_to_login_btn()
    sleep(2)


@Then('I am again on the Signin page')
def step_impl(context):
    sleep(2)
    # expected_url = context.sign_up.URL()
    assert context.basepage.get_current_url() == context.sign_in.URL
    sleep(2)
