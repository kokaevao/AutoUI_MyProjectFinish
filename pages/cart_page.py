import time

import allure

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    pickup_radio_button = '//*[@id="shipping_method_0_local_pickup3"]'
    checkout_button = '//*[@id="post-5"]/div/div/div[2]/div/div/a'
    word_checkout = '//*[@id="post-6"]/header/h1'



    # Getters

    def get_pickup_radio_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup_radio_button)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_word_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_checkout)))

    # Actions

    def click_pickup_radio_button(self):
        self.get_pickup_radio_button().click()
        print("Нажали на радио кнопку Самовывоз (Бауманская 9)")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Нажали на кнопку Оформить заказ")

    # Method

    def confirmation_cart_snapback_yankees_red(self):
        with allure.step("Проверка корректности добавленного товара"):
            Logger.add_start_step(method='confirmation_cart_snapback_yankees_red')
            self.click_pickup_radio_button()
            time.sleep(2)
            self.click_checkout_button()
            self.assert_word(self.get_word_checkout(), "Оформление заказа")
            self.asset_url("https://famshop.ru/checkout/")
            Logger.add_end_step(url=self.driver.current_url, method='confirmation_cart_snapback_yankees_red')



