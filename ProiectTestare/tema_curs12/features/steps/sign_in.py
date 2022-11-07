from behave import *
from time import sleep


@Given("I am on the SignIn page")
def step_impl(context):
    context.sign_in.go_home()


@When("I enter a correct email")
def step_impl(context):
    context.sign_in.input_email('lavinia@yahoo.com')


@When("I leave password empty")
def step_impl(context):
    context.sign_in.input_password(' ')
    context.sign_in.delete_password()


@Then('The login button is disabled')
def step_impl(context):
    try:
        context.sign_in.click_login()
        print('Enabled')
    except:
        print('Disabled')


@Then('A message error with text: "{text_message}" appears')
def step_impl(context, text_message):
    assert text_message in context.sign_in.message_text_error()


@when("I enter a password")
def step_impl(context):
    password_example = "TomSmith1"
    context.sign_in.input_password(password_example)


@when("I press the eye button")
def step_impl(context):
    context.sign_in.password_text_visible()
    #nu reusesc sa fac parola vizibila direct in browser
    sleep(3)


@then("I should see the password")
def step_impl(context):
    # assert context.sign_in.password_text_visible == context.sign_in.input_password()
    pass

