from os import link
import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class use_select_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_use_select(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_custom_select.asp')
        self.driver.implicitly_wait(10)
        my_select = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/select')
        my_option = my_select.find_elements_by_tag_name('option')
        self.driver.implicitly_wait(3)
        for op in my_option:
            print(f'{op.get_attribute("value")}: {op.get_attribute("innerText")}')
            op.click()
        selected = Select(driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/select'))
        selected.select_by_visible_text('Audi')
        time.sleep(1)
        # link_python = driver.find_elements_by_xpath('//*[@id="main"]/div[2]')
        hover = ActionChains(driver).move_to_element(my_select)
        hover.perform()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
	unittest.main()