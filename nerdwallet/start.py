import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class StartWeb(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_start(self):
        driver = self.driver
        driver.get('https://www.nerdwallet.com/banking/calculator/compound-interest-calculator')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)