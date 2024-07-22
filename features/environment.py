
from pages import base
from logs import logs_config
import logging
log = logs_config.get_logs()


base_url = "https://preprod.inmobiusinfinitylearn.com/home"

def before_all(context):
    context.driver = logging.FileHandler.selenium_driver = base.launch_url()
    context.driver.set_page_load_timeout(120)
    context.driver.get(base_url)
    context.driver.maximize_window()

def after_all(context):
    pass
    # context.driver.quit()
    
