from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    menu_hair_dryer = '//*[@id="__next"]/div[1]/main/div/div/div[14]/div/div[2]/div[1]/div/div[2]/div[1]/a'

    # Getters
    def get_hair_dryer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_hair_dryer)))

    # Actions
    def click_menu_hair_dryer(self):
        self.get_hair_dryer().click()
        print("Выбрали категорию товаров Фены")


    # Method

    def select_menu_hair_dryer(self):
        self.click_menu_hair_dryer()
        self.get_current_url()
        self.asset_url('https://www.eldorado.ru/c/feny/')
