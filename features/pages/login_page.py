from locators.login_locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from logs import logs_config

log = logs_config.get_logs()

class LOGIN_PAGE:
    def __init__(self, driver):
        self.driver = driver
    
    def student_login_page(self):
        status = False
        try:
            # self.driver.find_element(By.XPATH, "//div[@id='signup']/div/div[1]").click()
            # student_login_page = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@id='signup']/div/div[1]")))
            student_login = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((list(STUDENT_PAGE_XPATH.keys())[0],list(STUDENT_PAGE_XPATH.values())[0])))
            student_login.click()
            status = True
        except Exception as e:
            log.error(f"Exception from Pages: {e}")
        return status
        

    def student_user_name_field(self,uname):
        status = False
        try:
            # username_field = WebDriverWait(self.driver).until(EC.presence_of_element_located((list(ADMISSION_INPUT_XPATH.keys())[0], list(ADMISSION_INPUT_XPATH.values())[0])))
            username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((list(ADMISSION_INPUT_XPATH.keys())[0],list(ADMISSION_INPUT_XPATH.values())[0])))
            username_field.send_keys(uname)
            status = True
        except Exception as e:
            log.error(f"Exception from Pages: {e}")
        return status
    def student_pwd(self, pwd):
        status = False
        try:
            user_pwd_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((list(PASSWORD_INPUT_XPATH.keys())[0], list(PASSWORD_INPUT_XPATH.values())[0])))
            user_pwd_field.send_keys(pwd)
            log.info(pwd)
            status = True
        except Exception as e:
            log.error(f"Exception from Pages: {e}")
        return status
    def student_login_btn(self):
        status = False
        try:
            login_btn = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((list(LOGIN_BUTTON_XPATH.keys())[0], list(LOGIN_BUTTON_XPATH.values())[0])))
            login_btn.click()
            status = True
        except Exception as e:
            log.error(f"Exception from pages: {e}")
        return status
    
    def validate_credential(self, expected_login_text):
        status = False
        try:
            #webdriver present of elemt alsways accepts Tuple so Extra Braket is there
            #(list(LOGIN_ID_XPATH.keys())[0], list(LOGIN_ID_XPATH.values())[0]) using"()"" convert in Tuble from dictionary.
            validate_text_elemnt = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((list(LOGIN_ID_XPATH.keys())[0], list(LOGIN_ID_XPATH.values())[0])))
            validate_text=validate_text_elemnt.text
            log.info(f"expected_login_text: {expected_login_text}")
            log.info(f"validate_text: {validate_text}")
            validate_text == expected_login_text
            status = True
        except Exception as e:
            log.error(f"Exception from Pages: {e}")
        return status
    