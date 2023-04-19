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
        return self.find_elements(Locators.RENTAL_PERIOD_FIELD)[option].click()

    @allure.step('Выбор цвета')
    def choose_color(self, option: int):
        return self.find_elements(Locators.COLOR_CHECKBOXES)[option].click()
