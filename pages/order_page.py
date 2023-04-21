import re

from pages.base_page import BasePage
from utils.locators import YaScooterOrderPageLocator as Locators
import allure


class YaScooterOrderPage(BasePage):
    @allure.step('Ввод фамилии')
    def input_last_name(self, last_name: str):
        return self.find_element(Locators.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step('Ввод имени')
    def input_first_name(self, first_name: str):
        return self.find_element(Locators.FIRST_NAME_INPUT).send_keys(first_name)

    @allure.step('Ввод адреса')
    def input_address(self, address: str):
        return self.find_element(Locators.ADDRESS_INPUT).send_keys(address)

    @allure.step('Выбор метро')
    def choose_subway(self, subway_name: str):
        self.find_element(Locators.SUBWAY_FIELD).click()
        return self.find_element(Locators.SUBWAY_HINT_BUTTON(subway_name)).click()

    @allure.step('Ввод номера телефона')
    def input_telephone_number(self, telephone_number: str):
        return self.find_element(Locators.TELEPHONE_NUMBER_FIELD).send_keys(telephone_number)

    @allure.step('Перейти на следующий этап заказа')
    def go_next(self):
        return self.find_element(Locators.NEXT_BUTTON).click()

    @allure.step('Ввод даты')
    def input_date(self, date: str):
        return self.find_element(Locators.DATE_FIELD).send_keys(date)

    @allure.step('Выбор периода аренды')
    def choose_rental_period(self, option: int):
        self.find_element(Locators.RENTAL_PERIOD_FIELD).click()
        return self.find_elements(Locators.RENTAL_PERIOD_LIST)[option].click()

    @allure.step('Выбор цвета')
    def choose_color(self, option: int):
        return self.find_elements(Locators.COLOR_CHECKBOXES)[option].click()

    @allure.step('Комментарий для курьера')
    def input_comment(self, comment_text):
        return self.find_element(Locators.COMMENT_FOR_COURIER_FIELD).send_keys(comment_text)

    @allure.step('Нажать "Заказать"')
    def click_order(self):
        return self.find_element(Locators.ORDER_BUTTON).click()

    @allure.step('Подтвердить заказ')
    def click_accept_order(self):
        return self.find_element(Locators.ACCEPT_ORDER_BUTTON).click()

    @allure.step('Вычитать номер заказа')
    def get_order_number(self):
        about_order_text = self.find_element(Locators.ORDER_COMPLETED_INFO).text
        return ''.join(re.findall('[0-9]', about_order_text))

    @allure.step('Перейти к статусу заказа')
    def click_go_to_status(self):
        return self.find_element(Locators.SHOW_STATUS_BUTTON).click()
    
    @allure.step('Заполнить данные на этапе "Для кого самокат"')
    def fill_user_data(self, data_set: dict):
        self.input_first_name(data_set['first_name'])
        self.input_last_name(data_set['last_name'])
        self.input_address(data_set['address'])
        self.choose_subway(data_set['subway_name'])
        self.input_telephone_number(data_set['telepthone_number'])

    @allure.step('Заполнить данные на этапе "Про аренду"')
    def fill_rent_data(self, data_set: dict):
        self.input_date(data_set['date'])
        self.choose_rental_period(data_set['rental_period'])
        for option in data_set['color']:
            self.choose_color(option)
        self.input_comment(data_set['comment_for_courier'])
