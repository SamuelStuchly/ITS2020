from behave import *
from selenium.webdriver import ActionChains

from selenium.webdriver.support.expected_conditions import alert_is_present
import time

@given("there is a side menu")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="menu"]')



@given("there is a Catalog option")
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[1]/nav/ul/li[2]/a/span')



@when("I click Catalog option")
def step_impl(context):
    catalog = context.driver.find_element_by_xpath('//*[@id="catalog"]/a/i')
    catalog.click()
    hover = ActionChains(context.driver).move_to_element(catalog)
    hover.perform()



@then("Catalog option expands into multiple options")
def step_impl(context):
    expanded = context.driver.find_element_by_xpath('//*[@id="catalog"]/ul').get_attribute('aria_expanded')

    if expanded:
         pass
    else:
        # maybe it is howered over expanded but diferently
          try:
              #Products option
              context.driver.find_element_by_xpath('//*[@id="catalog"]/ul/li[2]/a')
          except Exception as e:
              raise e




@given("Catalog option on the side menu is expanded")
def step_impl(context):
    catalog = context.driver.find_element_by_xpath('//*[@id="catalog"]/a/i')
    catalog.click()
    hover = ActionChains(context.driver).move_to_element(catalog)
    hover.perform()



@given("there is a Products option")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="catalog"]/ul/li[2]/a')



@when("I click on the Products option")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="catalog"]/ul/li[2]/a').click()



@then("Products page is displayed")
def step_impl(context):
    text = context.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/h3').text
    assert text == 'Product List'



@given("a product is displayed in a product list")
def step_impl(context):
    if context.driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr/td').text == "No results!":
        raise AssertionError("Product List empty")



@when("I click on products Edit button")
def step_impl(context):
    product = context.driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[1]/td[8]/a')
    product_name = context.driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[1]/td[3]').text
    context.product_name = product_name
    product.click()



@then("I access its Edit Product page")
def step_impl(context):
    edit_page = context.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/h3').text


    assert edit_page == "Edit Product"

    assert context.driver.find_element_by_xpath('//*[@id="input-name1"]').get_attribute('value') == context.product_name




@given("I am on Edit Product page")
def step_impl(context):
    catalog = context.driver.find_element_by_xpath('//*[@id="catalog"]/a/i')
    catalog.click()
    hover = ActionChains(context.driver).move_to_element(catalog)
    hover.perform()

    context.driver.find_element_by_xpath('//*[@id="catalog"]/ul/li[2]/a').click()

    product = context.driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr/td[3]')
    context.product_name = product.text

    context.driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[1]/td[8]/a').click()



#probably useless
# TODO
@given("I edited some information")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="form-product"]/ul/li[2]').click()
    model_elem = context.driver.find_element_by_xpath('//*[@id="input-model"]')
    model_elem.send_keys(" Pro")
    context.product_model = model_elem.get_attribute('value')



@given("all required fields are filled")
def step_impl(context):
    assert context.driver.find_element_by_xpath('//*[@id="input-model"]').get_attribute('value') is not None
    context.driver.find_element_by_xpath('//*[@id="form-product"]/ul/li[1]/a').click()
    assert context.driver.find_element_by_xpath('//*[@id="input-name1"]').get_attribute('value') is not None
    assert context.driver.find_element_by_xpath('//*[@id="input-meta-title1"]').get_attribute('value') is not None



@when("I click the Save button")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button').click()



@then("edited information is saved")
def step_impl(context):
    assert alert_is_present()
    body_elem = context.driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[1]/td[4]').text

    assert body_elem == context.product_model






@when("I click Add New button")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/a').click()



@then("Add product page is displayed")
def step_impl(context):
    page_name = context.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/h3').text
    assert page_name == "Add Product"



@given("I am on the Add product page")
def step_impl(context):
    catalog = context.driver.find_element_by_xpath('//*[@id="catalog"]/a/i')
    catalog.click()
    hover = ActionChains(context.driver).move_to_element(catalog)
    hover.perform()

    context.driver.find_element_by_xpath('//*[@id="catalog"]/ul/li[2]/a').click()

    context.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/a').click()

    context.driver.find_element_by_xpath('//*[@id="form-product"]/ul/li[2]').click()

    context.driver.find_element_by_xpath('//*[@id="input-model"]').send_keys("Model 420")

    context.driver.find_element_by_xpath('//*[@id="form-product"]/ul/li[1]/a').click()
    context.driver.find_element_by_xpath('//*[@id="input-name1"]').send_keys("SuperPhone")
    context.driver.find_element_by_xpath('//*[@id="input-meta-title1"]').send_keys("SuperPhone_meta")




@then("new product is added")
def step_impl(context):
    # a success alert is displyes when new product is added
    assert alert_is_present()
