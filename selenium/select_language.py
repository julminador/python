import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select # Submodulo  para usar el dropdown

class LanguageOptions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com/')
        
    def test_sort_by(self):
        self.driver.find_element_by_xpath('//*[@id="nav"]/ol/li[5]/a').click()
        exposed_options = ['Position', 'Name', 'Price']
        active_options = []
        sort_by = Select(self.driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/select'))  # Accede a las opciones del dropdown
        # sort_by = Select(self.driver.find_elements_by_id('select-language'))
        self.assertEqual(3, len(sort_by.options)) # Compruba la cantidad de opciones

        for option in sort_by.options:
            active_options.append(option.text)
        
        self.assertListEqual(exposed_options,active_options) # Valida la lista de opciones disponibles y las opciones activas

        self.assertEqual('Position', sort_by.first_selected_option.text) # Verifica que "Position" sea la primera opción del dropdown

        sort_by.select_by_visible_text('Name') # Selecciona "Name"

        # Verifica que el sitio cambio en la url del sitio contiene "name"
        self.assertTrue('order=name' in self.driver.current_url)

        sort_by = Select(self.driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/select'))  # Accede a las opciones del dropdown
        sort_by.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)