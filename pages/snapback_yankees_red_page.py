import time

from selenium.webdriver import ActionChains

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Snapback_yankees_red_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    word_title_snapback_yankees_red = '//*[@id="product-75860"]/div[2]/h1'
    word_price_snapback_yankees_red = '//*[@id="product-75860"]/div[2]/p/span'
    word_card_price_snapback_yankees_red = '//*[@id="site-header-cart"]/li[1]/a/span[1]'
    select_size_snapback_yankees_red = '//*[@id="pa_size"]'
    add_card_snapback_yankees_red = '//*[@id="product-75860"]/div[2]/form/div/div[2]/button'
    word_add_card_snapback_yankees_red = '//*[@id="content"]/div/div[1]/div'

    # Getters

    def get_word_title_snapback_yankees_red(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_title_snapback_yankees_red)))

    def get_word_price_snapback_yankees_red(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_price_snapback_yankees_red)))

    def get_word_card_price_snapback_yankees_red(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_card_price_snapback_yankees_red)))

    def get_select_size_snapback_yankees_red(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size_snapback_yankees_red)))

    def get_add_card_snapback_yankees_red(self):
        return self.driver.find_element(By.XPATH, self.add_card_snapback_yankees_red)

    def get_word_add_card_snapback_yankees_red(self):
        return self.driver.find_element(By.XPATH, self.word_add_card_snapback_yankees_red)



    # Actions
    def click_select_size_snapback_yankees_red(self):
        Select(self.get_select_size_snapback_yankees_red()).select_by_value('sm')
        print("Выбрали размер бейсболки S/M")

    def click_add_card_snapback_yankees_red_button(self):
        self.get_add_card_snapback_yankees_red().click()
        print("Нажали кнопку Добавить в корзину")





    # Method

    def add_snapback_yankees_red(self):
        self.assert_word(self.get_word_title_snapback_yankees_red(), "Бейсболка 9FIFTY SNAPBACK MLB NEW YORK YANKEES ESSENTIAL RED")
        self.assert_word(self.get_word_price_snapback_yankees_red(), "4,599.00 Р")
        self.click_select_size_snapback_yankees_red()
        self.click_add_card_snapback_yankees_red_button()
        time.sleep(2)
        self.assert_word(self.get_word_add_card_snapback_yankees_red(), "Просмотр корзины\nВы отложили “Бейсболка 9FIFTY SNAPBACK MLB NEW YORK YANKEES ESSENTIAL RED” в свою корзину.")
        self.assert_word(self.get_word_price_snapback_yankees_red(), self.get_word_card_price_snapback_yankees_red().text[:-3])



