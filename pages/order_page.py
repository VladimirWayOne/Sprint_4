from pages.base_page import BasePage
from utils.locators import YaScooterOrderPageLocator as Locators


class YaScooterOrderPage(BasePage):
    def input_last_name(self, last_name: str):
        return self.find_element(Locators.LAST_NAME_INPUT).send_keys(last_name)

    def input_first_name(self, first_name: str):
        return self.find_element(Locators.FIRST_NAME_INPUT).send_keys(first_name)

    def input_address(self, address: str):
        return self.find_element(Locators.ADDRESS_INPUT).send_keys(address)

    def choose_subway(self, subway_name: str):
        self.find_element(Locators.SUBWAY_FIELD).click()
        return self.find_element(Locators.SUBWAY_HINT_BUTTON(subway_name)).click()

    def input_telephone_number(self, telephone_number: str):
        return self.find_element(Locators.TELEPHONE_NUMBER_FIELD).send_keys(telephone_number)

    def go_next(self):
        return self.find_element(Locators.NEXT_BUTTON).click()

    def input_date(self, date: str):
        return self.find_element(Locators.DATE_FIELD).send_keys(date)

    def choose_rental_period(self, option: int):
        self.find_element(Locators.RENTAL_PERIOD_FIELD).click()
        return self.find_elements(Locators.RENTAL_PERIOD_FIELD)[option].click()

    def choose_color(self, option: int):
        return self.find_elements(Locators.COLOR_CHECKBOXES)[option].click()
