import time

import allure

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from utilities.logger import Logger


class Snapback_yankees_red_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    select_size_snapback_yankees_red = '//*[@id="pa_size"]'
    add_card_snapback_yankees_red = '//*[@id="product-75860"]/div[2]/form/div/div[2]/button'
    word_add_card_snapback_yankees_red = '//*[@id="content"]/div/div[1]/div'
    go_to_card_button = '//*[@id="site-header-cart"]/li[1]/a'
    word_title_snapback_yankees_red_cart = '//*[@id="post-5"]/div/div/form/table/tbody/tr[1]/td[3]/a'
    word_price_snapback_yankees_red_cart = '//*[@id="post-5"]/div/div/form/table/tbody/tr[1]/td[4]/span'
    word_price_total_snapback_yankees_red_cart = '//*[@id="post-5"]/div/div/div[2]/div/table/tbody/tr[1]/td/span'
    word_price_snapback_yankees_red = '//*[@id="product-75860"]/div[2]/p/span'
    word_card_price_snapback_yankees_red = '//*[@id="site-header-cart"]/li[1]/a/span[1]'


    # Getters

    def get_select_size_snapback_yankees_red(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size_snapback_yankees_red)))

    def get_add_card_snapback_yankees_red(self):
        return self.driver.find_element(By.XPATH, self.add_card_snapback_yankees_red)

    def get_word_add_card_snapback_yankees_red(self):
        return self.driver.find_element(By.XPATH, self.word_add_card_snapback_yankees_red)

    def get_go_to_card_button(self):
        return self.driver.find_element(By.XPATH, self.go_to_card_button)

    def get_word_title_snapback_yankees_red_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_title_snapback_yankees_red_cart)))

    def get_word_price_snapback_yankees_red_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_price_snapback_yankees_red_cart)))

    def get_word_price_total_snapback_yankees_red_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_price_total_snapback_yankees_red_cart)))

    def get_word_price_snapback_yankees_red(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_price_snapback_yankees_red)))

    def get_word_card_price_snapback_yankees_red(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_card_price_snapback_yankees_red)))



    # Actions
    def click_select_size_snapback_yankees_red(self):
        Select(self.get_select_size_snapback_yankees_red()).select_by_value('sm')
        print("Выбрали размер бейсболки S/M")

    def click_add_card_snapback_yankees_red_button(self):
        self.get_add_card_snapback_yankees_red().click()
        print("Нажали кнопку Добавить в корзину")

    def click_go_to_card_button(self):
        self.get_go_to_card_button().click()
        print("Нажали кнопку Перехода в корзину")





    # Method

    def add_snapback_yankees_red(self):
        with allure.step("Добавление красной бейсболки Yankees в корзину"):
            Logger.add_start_step(method='add_snapback_yankees_red')
            self.click_select_size_snapback_yankees_red()
            self.click_add_card_snapback_yankees_red_button()
            time.sleep(2)
            self.assert_word(self.get_word_add_card_snapback_yankees_red(), "Просмотр корзины\nВы отложили “Бейсболка 9FIFTY SNAPBACK MLB NEW YORK YANKEES ESSENTIAL RED” в свою корзину.")
            self.assert_word(self.get_word_price_snapback_yankees_red(), self.get_word_card_price_snapback_yankees_red().text[:-3])
            self.click_go_to_card_button()
            self.asset_url("https://famshop.ru/cart/")
            self.assert_word(self.get_word_title_snapback_yankees_red_cart(), "Бейсболка 9FIFTY SNAPBACK MLB NEW YORK YANKEES ESSENTIAL RED - S/M")
            self.assert_word(self.get_word_price_snapback_yankees_red_cart(), self.get_word_price_total_snapback_yankees_red_cart().text)
            Logger.add_end_step(url=self.driver.current_url, method='add_snapback_yankees_red')



