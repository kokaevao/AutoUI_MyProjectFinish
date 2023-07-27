from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main_page(Base):

    url = 'https://famshop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    word_contact = '//*[@id="menu-item-447"]/a'
    category_men = '//*[@id="menu-item-124"]/a'
    word_men = '//*[@id="main"]/header/h1'



    #Getters

    def get_word_contact(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_contact)))

    def get_category_men(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_men)))


    def get_word_men(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_men)))




    #Actions


    def click_category_men(self):
        self.get_category_men().click()
        print("Перешли в категорию товаров 'Мужчины'")



    #Method

    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.asset_url("https://famshop.ru/")
        self.assert_word(self.get_word_contact(), "Контакты")


    def go_to_category_men(self):
        self.click_category_men()
        self.get_current_url()
        self.asset_url("https://famshop.ru/product-category/men/")
        self.assert_word(self.get_word_men(), "Мужчинам")







