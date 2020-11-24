from behave import *
from time import sleep
from selenium.webdriver.support.expected_conditions import alert_is_present

#
@given("at least one product is selected")
def step_impl(context):
    context.driver.find_element_by_xpath("//form[@id='form-product']/div/table/tbody/tr[14]/td/input").click()
    context.selected_item = context.driver.find_element_by_xpath("//form[@id='form-product']/div/table/tbody/tr[14]/td[3]").text



@when("I click delete button")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button[2]').click()
    sleep(2)
    obj = context.driver.switch_to.alert
    sleep(2)
    obj.accept()
    sleep(2)



@then("selected products are deleted")
def step_impl(context):
    assert alert_is_present()

    #assert context.driver.find_element_by_xpath("//form[@id='form-product']/div/table/tbody/tr[15]/td[3]").text != context.selected_item



@when("I click the Copy button")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button[1]/i').click()



@then("for each selected product a copy is added into Product list")
def step_impl(context):
    assert alert_is_present()
    assert context.driver.find_element_by_xpath("//form[@id='form-product']/div/table/tbody/tr[15]/td[3]").text == context.selected_item
