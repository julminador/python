import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class example_assert_equal(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.maximize_window()

    def test_assertEqual(self):
        driver = self.driver
        driver.get('https://www.amazon.com/')
        time.sleep(5)
        all =  driver.find_element_by_xpath('//*[@id="nav-hamburger-menu"]')
        all.click()
        time.sleep(2)
        kindle =  driver.find_element_by_xpath('//*[@id="hmenu-content"]/ul[1]/li[3]')

        mouse = ActionChains(driver)
        mouse.move_to_element(kindle)
        time.sleep(3)
        mouse.move_to_element(kindle).click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()