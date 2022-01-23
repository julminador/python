from lib2to3.pgen2 import driver
import secrets
import time
import unittest
from xml.dom import IndexSizeErr
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

class cycle_form(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(5)
        driver.maximize_window()

    def test_form(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/html/html_forms.asp')
        countPages = len(driver.window_handles)


        def complete_form(first_name, last_name, countPages):
            if countPages > 0:
                driver.switch_to.window(driver.window_handles[0])

            fname = driver.find_element_by_id('fname')
            lname = driver.find_element_by_id('lname')
            btn_submit = driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/div[3]/div/form/input[3]')
            actions = ActionChains(driver)

            actions.double_click(fname).perform()
            fname.send_keys(first_name)
            actions.double_click(lname).perform()
            lname.send_keys(last_name)
            btn_submit.click()
            print(first_name)
            print(last_name)
            countPages = len(driver.window_handles)

        with open('names.csv', encoding='utf-8') as file:
            for i, line in enumerate(file):
                info = (line)
                info = line.split(",")
                try:
                    first_name = info[0]
                    last_name = info[1]
                except IndexError:
                    first_name = 'null'
                    last_name = 'null'
                complete_form(first_name, last_name, countPages)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)