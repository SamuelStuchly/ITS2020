from behave import *
from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException




@given("I am on the Products page")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="button-menu"]/i').click()
    # expand catalog
    catalog = context.driver.find_element_by_xpath('//*[@id="catalog"]/a/i')
    catalog.click()
    # hover over to expand catalog
    hover = ActionChains(context.driver).move_to_element(catalog)
    hover.perform()

    context.driver.find_element_by_xpath('//*[@id="catalog"]/ul/li[2]/a').click()
    text = context.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/h3').text
    assert text == 'Product List'


# --------------------------------------------------------------

@given("I have set filters to desired values")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="input-name"]').send_keys("iPhone")
    context.filtered_name = 'iPhone'



@when("I press the filter button")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="button-filter"]').click()



@then("filtered Product list is displayed")
def step_impl(context):
    assert context.filtered_name == context.driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr/td[3]').text
    try :
        context.driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[2]/td[3]').text
    except Exception as e:
        if type(e) is not NoSuchElementException:
            raise e

