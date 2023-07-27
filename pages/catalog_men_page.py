from selenium.webdriver import ActionChains

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Catalog_men_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_sort = '//*[@id="main"]/div[1]/form/select'
    color_checkbox_red = '//*[@id="woocommerce_layered_nav-9"]/ul/li[14]/a'
    license_checkbox_mlb = '//*[@id="woocommerce_layered_nav-6"]/ul/li[2]/a'
    size_checkbox_sm = '//*[@id="woocommerce_layered_nav-7"]/ul/li[11]/a'
    price_scroolbar = '//*[@id="woocommerce_price_filter-3"]/form/div/div[1]'
    price_filter_button = '//*[@id="woocommerce_price_filter-3"]/form/div/div[2]/button'
    word_snapback_yankees_red = '//*[@id="main"]/ul/li/a[1]/h2'
    select_size_snapback_yankees_red_button = '//*[@id="main"]/ul/li/a[2]'




    # Getters

    def get_select_sort(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_sort)))

    def get_color_checkbox_red(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color_checkbox_red)))

    def get_license_checkbox_mlb(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.license_checkbox_mlb)))

    def get_size_checkbox_sm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_checkbox_sm)))

    def get_price_scroolbar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_scroolbar)))

    def get_price_filter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filter_button)))

    def get_word_snapback_yankees_red(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_snapback_yankees_red)))

    def get_select_size_snapback_yankees_red_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size_snapback_yankees_red_button)))

    # Actions

    def click_select_rating_sort(self):
        Select(self.get_select_sort()).select_by_value('rating')
        print("Выбрали сортировку по рейтингу")

    def click_color_checkbox_red(self):
        self.get_color_checkbox_red().click()
        print("Выбрали фильтр цвет Красный")

    def click_license_checkbox_mlb(self):
        self.get_license_checkbox_mlb().click()
        print("Выбрали фильтр лицензию MLB")

    def click_size_checkbox_sm(self):
        self.get_size_checkbox_sm().click()
        print("Выбрали фильтр размер S/M")

    def select_price_scroolbar_75(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_price_scroolbar()).move_by_offset(50, 0).release().perform()
        print("Передвинули ползунок на 75%")

    def click_price_filter_button(self):
        self.get_price_filter_button().click()
        print("Нажали кнопку Фильтровать")

    def click_select_size_snapback_yankees_red_button(self):
        self.get_select_size_snapback_yankees_red_button().click()
        print("Нажали кнопку Выбрать размер")


    # Method

    def select_snapback_yankees_red(self):
        self.click_select_rating_sort()
        self.click_color_checkbox_red()
        self.click_license_checkbox_mlb()
        self.click_size_checkbox_sm()
        self.select_price_scroolbar_75()
        self.click_price_filter_button()
        self.assert_word(self.get_word_snapback_yankees_red(), "Бейсболка 9FIFTY SNAPBACK MLB NEW YORK YANKEES ESSENTIAL RED")
        self.click_select_size_snapback_yankees_red_button()
        self.asset_url("https://famshop.ru/shop/beisbolka-9fifty-snapback-mlb-new-york-yankees-essential-red/")


