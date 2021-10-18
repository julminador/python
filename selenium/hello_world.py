import unittest
from pyunitreport import HTMLTestRunner # Manejo de pruebas y reportes
from selenium import webdriver # La comunicación con el navegador


class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls): # Test feature
        """Prepara el entorno de la prueba"""
        # cls.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        cls.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        cls.driver.implicitly_wait(10)

    def test_hello_world(self): # Unit test
        """Caso de prueba: acciones a automatizar"""
        driver = self.driver
        driver.get('https://www.platzi.com')

    @classmethod
    def tearDownClass(cls): # Test feature de salida
        """Acciones para finalizar"""
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))