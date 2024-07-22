from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



def launch_url():
    options = Options()
    options.add_experimental_option("detach", True)
    driver_path = r"C:\Users\arun\OneDrive\Documents\inmobius_automation\driver\chromedriver.exe"
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    #driver = webdriver.Chrome(EdgeChromiumDriverManager().install(), options=options)
    return driver