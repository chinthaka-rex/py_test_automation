from behave import *

from features.pages import validating_textbox_page


@given('launch browser')
def launch_browser(context):
    validating_textbox_page.browser_load(context)


@when('navigate to the demoqa textbox page "{web_address}"')
def navigate_to_the_demoqa_text_page(context, web_address):
    validating_textbox_page.navigate_to_the_demoqa_text_page(context, web_address)


@then('enter the name into fullname "{fuName}" textbox')
def enter_fullname(context, fuName):
    validating_textbox_page.enter_the_fullname(context, fuName)


@then('enter the name into email "{email}" textbox')
def enter_email(context, email):
    validating_textbox_page.enter_email(context, email)


@then('enter the name into current address "{cAddress}" textbox')
def enter_current_address(context, cAddress):
    validating_textbox_page.enter_current_address(context, cAddress)


@then('enter the name into permanent address "{pAddress}" textbox')
def enter_permanent_address(context, pAddress):
    validating_textbox_page.enter_permanent_address(context, pAddress)


@then('click on the submit button')
def click_on_the_submit_button(context):
    validating_textbox_page.click_submit_btn(context)


@when('check the name inserted is equal to "{in_name}"')
def check_name(context, in_name):
    name_txt = validating_textbox_page.verify_the_name(context)
    assert name_txt == in_name


@when('check the email inserted is equal to "{in_email}"')
def check_email(context, in_email):
    email_txt = validating_textbox_page.verify_the_email(context)
    assert email_txt == in_email


@when('check the current address inserted is equal to "{in_c_add}"')
def check_current_address(context, in_c_add):
    c_add_txt = validating_textbox_page.verify_the_c_address(context)
    assert c_add_txt == in_c_add


@then('check the permanent address inserted is equal to "{in_p_add}"')
def check_permanent_address(context, in_p_add):
    p_add_txt = validating_textbox_page.verify_the_p_address(context)
    assert p_add_txt == in_p_add
