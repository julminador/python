import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class RegsterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.instagram.com/p/CX7RbCBJrjS/')

    def test_new_user(self):
        driver = self.driver
        driver.get_screenshot_as_file("C:\personalProjects\python\selenium\screenshot\my_poio.png")

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)