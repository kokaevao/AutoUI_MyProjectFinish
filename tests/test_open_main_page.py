import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from selenium.webdriver.chrome.service import Service

from pages.catalog_men_page import Catalog_men_page
from pages.snapback_yankees_red_page import Snapback_yankees_red_page
from pages.main_page import Main_page



def test_open_main():
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    options = webdriver.ChromeOptions()
    options.set_capability("loggingPrefs", {'performance': 'ALL'})
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\akokaev\\Desktop\\Learn_Python\\AutoUI_MyProjectFinish\\chromedriver.exe')
    driver = webdriver.Chrome(desired_capabilities=caps, options=options, service=g)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')





    print("Старт Теста")

    mp = Main_page(driver)
    mp.open_main_page()
    mp.go_to_category_men()

    cmp = Catalog_men_page(driver)
    cmp.select_snapback_yankees_red()

    syrp = Snapback_yankees_red_page(driver)
    syrp.add_snapback_yankees_red()




    print("Финиш теста")


