from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pages.catalog_page import Catalog_page
from pages.main_page import Main_page


def test_open_main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\akokaev\\Desktop\\Learn_Python\\AutoUI_MyProjectFinish\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    print("Start test open main")

    mp = Main_page(driver)
    mp.open_main_page()
    mp.go_to_catalog()

    cp = Catalog_page(driver)
    cp.select_menu_hair_dryer()

    driver.quit()
    print("Finish test open main")


