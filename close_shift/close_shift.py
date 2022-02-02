import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class close_shift(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(5)
        driver.maximize_window()

    def test_log_in(self):
        driver = self.driver
        driver.get("http://172.17.8.9/appmaster/")
        user_acount = '1032507144'
        user_password = '1032507144'
        user_input = driver.find_element_by_name('usuario')
        password_input = driver.find_element_by_name('password')
        log_in_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/input')
        user_input.send_keys(user_acount)
        password_input.send_keys(user_password)
        log_in_button.click()
        driver.implicitly_wait(5)
        driver.get("http://172.17.8.9/appmaster/?crm=11&CIU")
        driver.implicitly_wait(5)
        driver.switch_to.frame(driver.find_element_by_name('iframe_sitio'))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        end_shift_button = driver.find_element_by_id('turno_fin')
        end_shift_button.click()
        confirm_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]')
        confirm_button.click()
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("no alert")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)