from behave import *
from pages.login_page import LOGIN_PAGE
from locators import login_locators

from logs import logs_config
log = logs_config.get_logs()


# ------------------------------Click on Login with correct Login and Password.------------------------------
@given('I am on the login page')
def student_login(context):
    status = False
    try:
        login_page = LOGIN_PAGE(context.driver)
        login_page.student_login_page()
        status = True
    except Exception as e:
        log.error(f" Exception from Steps: {e}")
    assert status is True



@when('I enter username "{uname}"')
def login_btn(context, uname):
    status = False
    try:
        login_page = LOGIN_PAGE(context.driver)
        login_page.student_user_name_field(uname)
        status = True
    except Exception as e:
        log.error(f"Exception from Steps: {e}")
    assert status is True


@when('I enter password "{pwd}"')
def step_impl(context, pwd):
    status = False
    try:
        enter_pwd = LOGIN_PAGE(context.driver)
        enter_pwd.student_pwd(pwd)
        status = True
    except Exception as e:
        log.error(f"Exceptions from Steps: {e}")
    assert status is True

@when("I click the login button")
def step_impl(context):
    status = False
    try:
        click_login = LOGIN_PAGE(context.driver)
        click_login.student_login_btn()
        status = True
    except Exception as e:
        log.error(f"Exceptions from Steps: {e}")
    assert status is True


@then('It should display "{expected_login_text}" after logged in successfully')
def validate_login(context, expected_login_text):
    status = False
    try:
        validate = LOGIN_PAGE(context.driver)
        validate.validate_credential(expected_login_text)
        status = True
    except Exception as e:
        log.error(f"Exception from Steps:{e}")
    assert status is True

