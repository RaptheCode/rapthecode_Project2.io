from selenium import webdriver

class video():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\chromedriver')

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        viedo1= self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        viedo1.click()


