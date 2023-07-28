import time

import allure

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class Checkout_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    name = '//*[@id="billing_first_name"]'
    phone = '//*[@id="billing_phone"]'
    email = '//*[@id="billing_email"]'
    word_title_snapback_yankees_red_checkout = '//*[@id="order_review"]/table/tbody/tr/td[1]'
    word_price_subtotal_snapback_yankees_red_checkout = '//*[@id="order_review"]/table/tfoot/tr[1]/td/span'
    word_price_total_snapback_yankees_red_checkout = '//*[@id="order_review"]/table/tfoot/tr[3]/td/strong/span'
    valide_purchase_button = '//*[@id="place_order"]'
    word_checkout_total = '//*[@id="post-6"]/header/h1'
    word_price_total_snapback_yankees_red_finish = '//*[@id="post-6"]/div/div/ul/li[3]/strong/span'




    # Getters

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_word_title_snapback_yankees_red_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_title_snapback_yankees_red_checkout)))

    def get_word_price_subtotal_snapback_yankees_red_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_price_subtotal_snapback_yankees_red_checkout)))

    def get_word_price_total_snapback_yankees_red_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_price_total_snapback_yankees_red_checkout)))

    def get_valide_purchase_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.valide_purchase_button)))

    def get_word_checkout_total(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_checkout_total)))

    def get_word_price_total_snapback_yankees_red_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_price_total_snapback_yankees_red_finish)))

    # Actions

    def input_name(self, name):
        self.get_name().send_keys(name)
        print("Ввели имя покупателя")

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print("Ввели контактный телефон")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Ввели контактный емейл")

    def click_valide_purchase_button(self):
        self.get_valide_purchase_button().click()
        print("Нажали кнопку Подтвердить заказ")

    # Methods

    def checkout_snapback_yankees_red(self):
        with allure.step("Оформление заказа красной бейсболки Yankees"):
            Logger.add_start_step(method='checkout_snapback_yankees_red')
            self.input_name("Виктор")
            self.input_phone("9099998877")
            self.input_email("test@mail.ru")
            self.assert_word(self.get_word_title_snapback_yankees_red_checkout(), "Бейсболка 9FIFTY SNAPBACK MLB NEW YORK YANKEES ESSENTIAL RED - S/M  × 1")
            self.assert_word(self.get_word_price_subtotal_snapback_yankees_red_checkout(), self.get_word_price_total_snapback_yankees_red_checkout().text)
            self.click_valide_purchase_button()
            self.assert_word(self.get_word_checkout_total(), "Оформление заказа")
            self.assert_word(self.get_word_price_total_snapback_yankees_red_finish(), "4,599.00 Р")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='checkout_snapback_yankees_red')
