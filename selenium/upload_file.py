import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class upload_file(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.maximize_window()

    def test_upload_file(self):
        driver = self.driver
        driver.get('https://e2-bot.com/GestorReclamos/')
        driver.find_element_by_id('Usuario').send_keys('1032507144')
        driver.find_element_by_id('Password').send_keys('1032507144')
        driver.find_element_by_id('btnIngresar').click()
        driver.implicitly_wait(5)
        driver.find_element_by_id('file').send_keys('C:/Users/julminador/Downloads/Cargue_reclamos.xlsx')
        driver.find_element_by_id('btnCargar').click()
        driver.implicitly_wait(5)
        driver.find_element_by_id('BtnGuardarCargueCasos').click()
        driver.execute_script('window.scroll(0, 10000)')
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="TablaRepetidosExistentes_wrapper"]/div[2]/div[1]/a').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()