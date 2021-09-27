import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloWorld(unittest.TestCase):

    def setUp(self):
        """Prepara el entorno de la prueba"""
        # driver = self.driver
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        # self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        self.driver.implicitly_wait(10)

    def test_hello_world(self):
        """Caso de prueba: acciones a automatizar"""
        driver = self.driver
        driver.get('https://www.platzi.com')

    def tearDown(self):
        """Acciones para finalizar"""
        return super().tearDown()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))