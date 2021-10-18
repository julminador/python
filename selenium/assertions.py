import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException # Manejo de excepciones para los assertions
from selenium.webdriver.common.by import By # Llama a las excepciones que queremos validar

class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = self.driver
        # driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://demo.onestepcheckout.com/")

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'newsletter'))

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        """Identifica si está presente el elemento
        
        how: tipo de selector
        what: valor"""
        try:
            self.driver.find_element(by = how, value = what) 
        except NoSuchElementException as variable:
            return False
        return True