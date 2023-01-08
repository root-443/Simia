from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver import ActionChains
class CodyWeb :



    def __init__(self):
        print('init')
        self=''


    def goTo(self,url):
        global driver
        global options
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')
        driver = webdriver.Chrome(r"chromedriver.exe", options=options)
        driver.get(url)




    def Gsearch(self,item):
        search_bar = driver.find_element_by_name('q') # pour google
        search_bar.send_keys(item)
        search_bar.send_keys(Keys.ENTER)




    def getImage(self,cls):
        print("Searching for images")
        images = driver.find_elements_by_class_name(cls)
        for image in images:
            print(image.get_attribute('src'))



    def getItemName(self,classs):
        print("Searching for prices")
        ITEMS = driver.find_elements_by_class_name(classs)
        for i in ITEMS:
            print(i.text)

        #Base de donne pour plus tard

    def getPrice(self,classs):
        print("searching for prices")
        PRIX = driver.find_elements_by_class_name(classs)
        for p in PRIX:
            print(p.text)


    def Google(self,item):
        self.goTo("https://google.com")
        self.Gsearch(item)
        self.click()
        self.ExtractUrl()
        with open('sites.txt', 'w') as sites:
            print()


    def ExtractUrl(self):
        page = driver.page_source
        Text = page
        URLS = []
        URLS = (re.findall("(?P<url>https?://[^\s]+)", Text))
        with open('sites.txt', 'w') as filehandle:
            for listitem in URLS:
                filehandle.write('%s\n' % listitem)

    def close(self):
        driver.close()

    def FindProducts(self,site,item,cls1,cls3,cls4,cls5):
        timeout = 500
        self.goTo(site)
        self.search(cls1,item)
        main_window = driver.current_url
        print("Now navigating on " + driver.current_url)
        self.getItemName(cls3)
        self.getPrice(cls4)
        ITEMS = driver.find_elements_by_class_name(cls3)
        for i in ITEMS:

            ActionChains(driver).context_click(i).key_down(Keys.CONTROL).click(i).perform()
            ActionChains(driver).context_click(i).key_down(Keys.ESCAPE).perform()
            ActionChains(driver).context_click("body").key_down(Keys.CONTROL).key_down("2").perform()
            print(driver.current_url)
            self.getImage(cls5)
            ActionChains(driver).context_click("body").key_down(Keys.CONTROL).key_down("w").perform()

    def search(self,name,item):
        search_bar = driver.find_elements_by_name(name)
        search_bar[0].send_keys(item)
        search_bar[0].send_keys(Keys.ENTER)



