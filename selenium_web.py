from selenium import webdriver
import os
class infow():
    def __init__(self):
        self.driver = webdriver.Chrome('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\chromedriver')

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()
