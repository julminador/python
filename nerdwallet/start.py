import time
import unittest
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class StartWeb(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(10)


    def test_open_wallet(self):
        driver = self.driver
        driver.get('https://www.nerdwallet.com/banking/calculator/compound-interest-calculator')
        driver.execute_script('window.open("");')


    def test_open_window(self):
        driver = self.driver
        driver.switch_to.window(driver.window_handles[1])
        driver.get('https://www.twitter.com/julminador')


    def test_return_to_wallet(self):
        driver = self.driver
        driver.switch_to.window(driver.window_handles[0])
        initial_deposit = driver.find_element_by_xpath('//*[@id="form_view_compound_interest"]/div/div[2]/div[1]/label/div/input')
        initial_deposit.send_keys(Keys.CONTROL + 'a')
        initial_deposit.send_keys(Keys.DELETE)
        initial_deposit.send_keys('250')
        contributions = driver.find_element_by_xpath('//*[@id="form_view_compound_interest"]/div/div[2]/div[2]/label/div/input')
        contributions.send_keys(Keys.CONTROL + 'a')
        contributions.send_keys(Keys.DELETE)
        contributions.send_keys('50')
        monthly = driver.find_element_by_xpath('//*[@id="form_view_compound_interest"]/div/div[2]/div[4]/label/div/div[1]/div/div[3]')
        monthly.click()
        driver.execute_script("window.scrollTo(0, 300)")
        investment_time_span = driver.find_element_by_xpath('//*[@id="form_view_compound_interest"]/div/div[2]/div[4]/label/div/div[1]/div/div[3]')
        for i in range(4):
            investment_time_span.click()
        estimated_rate_of_return = driver.find_element_by_xpath('//*[@id="form_view_compound_interest"]/div/div[2]/div[5]/label/div/input')
        estimated_rate_of_return.send_keys(Keys.CONTROL + 'a')
        estimated_rate_of_return.send_keys(Keys.DELETE)
        estimated_rate_of_return.send_keys('7.15')
        compound_frequency = driver.find_element_by_xpath('//*[@id="form_view_compound_interest"]/div/div[2]/div[6]/label/div/label[2]/span/span/span[2]')
        compound_frequency.click()
        time.sleep(10)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)