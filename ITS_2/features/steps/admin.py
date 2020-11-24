from behave import *
from selenium.common.exceptions import NoSuchElementException , WebDriverException
from selenium.webdriver.support.expected_conditions import alert_is_present
import time 


# ==================== Scenario: Log in as Admin ==================== #

@given("I am on the admin login page")
def step_impl(context):


    context.driver.get("http://mat.fit.vutbr.cz:8101/admin/")

    assert "Administration" in context.driver.title


@when("I input admin username and password")
def step_impl(context):
    name_elem = context.driver.find_element_by_id('input-username')
    pswd_elem = context.driver.find_element_by_id('input-password')
    name_elem.send_keys("admin")
    pswd_elem.send_keys("admin")
    btn = context.driver.find_element_by_xpath("//button[@type='submit']")
    btn.click()

@then("I am logged in as Admin")
def step_impl(context):
    try:
        time.sleep(2)
        # Logout butteon
        context.driver.find_element_by_xpath('//*[@id="header"]/ul/li[4]/a')
        # Administrator span
        context.driver.find_element_by_xpath("/html/body/div[1]/nav/div[1]/div[2]/small")
    except Exception as e :
        if type(e) is WebDriverException:
            time.sleep(10)
            time.sleep(2)
            # Logout butteon
            context.driver.find_element_by_xpath('//*[@id="header"]/ul/li[4]/a')
            # Administrator span
            context.driver.find_element_by_xpath("/html/body/div[1]/nav/div[1]/div[2]/small")

@then("Admin view of page is displayed")
def step_impl(context):
    page_head = context.driver.find_element_by_xpath("//h1[contains(.,'Dashboard')]").text
    assert page_head == "Dashboard"
    assert context.driver.title == "Dashboard"

# --------------------------------------------------------------------------- #
# ==================== Scenario: Logout from Admin ==================== #
@given("I am logged in as Admin")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8101/admin/")


    name_elem = context.driver.find_element_by_id('input-username')
    pswd_elem = context.driver.find_element_by_id('input-password')
    name_elem.send_keys("admin")
    pswd_elem.send_keys("admin")
    btn = context.driver.find_element_by_xpath("//button[@type='submit']")
    btn.click()
    time.sleep(2)

    # Logout butteon
    context.driver.find_element_by_xpath('//*[@id="header"]/ul/li[4]/a')
    # Administrator span
    context.driver.find_element_by_xpath("/html/body/div[1]/nav/div[1]/div[2]/small")

@when("I click logout button")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="header"]/ul/li[4]/a').click()


@then("Admin login page is displayed")
def step_impl(context):
    assert "Administration" in context.driver.title


@then("I am logged out")
def step_impl(context):
    try:
        context.driver.find_element_by_xpath('//*[@id="header"]/ul/li[4]/a/span')
    except Exception as e:
        if type(e) is not NoSuchElementException:

            raise AssertionError("Not logged out!")



# --------------------------------------------------------------------------- #

# ==================== Scenario: Fail to log in as Admin ==================== #

# @given("I am on the admin login page")

@when("I input wrong username or password")
def step_impl(context):
    name_elem = context.driver.find_element_by_id('input-username')
    pswd_elem = context.driver.find_element_by_id('input-password')
    name_elem.send_keys("admin1234")
    pswd_elem.send_keys("admin1234")
    btn = context.driver.find_element_by_xpath("//button[@type='submit']")
    btn.click()

@then("I am not logged in as admin")
def step_impl(context):
    assert "Administration" in context.driver.title

@then("warning is displayed")
def step_impl(context):
    assert alert_is_present()


# --------------------------------------------------------------------------- #


