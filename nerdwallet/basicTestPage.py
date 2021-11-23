import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StartWeb(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_growing_clickable(self):
        driver = self.driver
        driver.get('https://testpages.herokuapp.com/styled/challenges/growing-clickable.html')
        grow_button = driver.find_element_by_id('growbutton')
        time.sleep(5)
        grow_button.click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)