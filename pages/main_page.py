from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main_page(Base):

    url = 'https://www.eldorado.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog = '//*[@id="__next"]/div[1]/div[1]/nav/ul/li[1]/a'
    word_login_and_registration = '//*[@id="__next"]/div[1]/header/div[2]/div/div[2]/button'
    word_catalog = '//*[@id="__next"]/div[1]/main/div/div/h1'



    #Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_word_login_and_registration(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_login_and_registration)))

    def get_word_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_catalog)))




    #Actions


    def click_catalog(self):
        self.get_catalog().click()
        print("Перешли в каталог")



    #Method

    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.assert_word(self.get_word_login_and_registration(), "Вход или регистрация")


    def go_to_catalog(self):
        self.click_catalog()
        self.get_current_url()
        self.assert_word(self.get_word_catalog(), f'Каталог товаров «Эльдорадо»')







