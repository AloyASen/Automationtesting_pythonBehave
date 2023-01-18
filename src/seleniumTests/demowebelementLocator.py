# scrape multiple elements in selenium Python 
# page link https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=1
# the best way to automate for all the pages is to loop for all the pages in the locator list

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By as BY

from webdriver_manager.chrome import ChromeDriverManager

class Item_Webscrapper(unittest.TestCase):
    # a global list for holding all the items being sold
    item_list = []
    def setUp(self):
        # setup the chrome driver for use in the session
        self.driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

    def _itemScaffolder(self, pageURL=''):
        self.driver.get(pageURL)
        title = self.driver.find_elements(BY.CLASS_NAME, 'title')
        price = self.driver.find_elements(BY.CLASS_NAME, 'price')
        description = self.driver.find_elements(BY.CLASS_NAME, 'description')
        rating = self.driver.find_elements(BY.CLASS_NAME, 'rating')

        for i in range(len(title)):
            self.item_list.append([title[i].text, price[i].text, description[i].text, rating[i].text ])

    def test_pageIterator(self):
        PageURL= 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'
        self.driver.get(PageURL)
        # depending on the count of disabled items in list
        nextpage=0
        while len(self.driver.find_elements(BY.XPATH, "//li[@class='page-item disabled']")) != int(2):
            nextpage =nextpage +1
            nextPageURL = PageURL+'?page=' +nextpage
            self.driver.implicitly_wait(2)
            self.driver.get(nextPageURL)
            self._itemScaffolder(nextPageURL)
        #display all the laptops available in the list 
        print(self.item_list)

    def tearDown(self):
        self.driver.close()
        print('final teardown')


if __name__ == '__main__':
    unittest.main()
