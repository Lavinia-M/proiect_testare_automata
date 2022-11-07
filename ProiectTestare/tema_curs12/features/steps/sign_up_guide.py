from behave import *
from time import sleep


@given(u'I am on the Sign in page')
def step_impl(context):
    context.sign_in.go_home()


@when(u'I click Sign up link')
def step_impl(context):
    context.sign_in.sign_up_button()
    sleep(2)


@when(u'I click Person option')
def step_impl(context):
    sleep(2)
    context.sign_up.person_button()


@when(u'I click continue')
def step_impl(context):
    context.sign_up.continue_button()


@when(u'I input "{first_name}" to the first name field')
def step_impl(context, first_name):
    context.sign_up.input_field(first_name)


# @when('I click continue')
# def step_impl(context):
#     context.sign_up.continue_button()


@when(u'I input "{last_name}" to the last name')
def step_impl(context, last_name):
    context.sign_up.input_field(last_name)


# @when('I click continue')
# def step_impl(context):
#     context.sign_up.continue_button()


@when(u'I input "{email}" to the email field')
def step_impl(context, email):
    context.sign_up.input_field(email)


@then(u'A message is displayed')
def step_impl(context, text):
    pass


@then(u'A message is not displayed')
def step_impl(context):
    pass
