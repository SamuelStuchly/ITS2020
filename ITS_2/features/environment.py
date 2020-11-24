import behave
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def before_scenario(context,scenario):
    dp = {'browserName': 'chrome', 'marionette': 'true',
            'javascriptEnabled': 'true'}

    context.driver = webdriver.Remote(
            command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',
            desired_capabilities=dp)
#                desired_capabilities=DesiredCapabilities.FIREFOX)



    context.driver.implicitly_wait(15)
    context.base_url = "http://mat.fit.vutbr.cz:8101/admin/"



def after_scenario(context,scenario):
    context.driver.quit()
