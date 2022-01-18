import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class example_assert_equal(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.maximize_window()
        driver.get('https://es.wikipedia.org/wiki/Wikipedia:Portada')

    def test_assertEqual(self):
        driver = self.driver
        web_tittle = driver.title
        self.assertEqual('Wikipedia, la enciclopedia libre', web_tittle, 'Is not a same tittle')

    def test_asserNottEqual(self):
        driver = self.driver
        web_tittle = driver.title
        self.assertNotEqual('Wikipedia, la enciclopedia libre', web_tittle, 'Is a same tittle')
    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()