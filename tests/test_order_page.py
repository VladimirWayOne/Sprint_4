import time

from pages.order_page import YaScooterOrderPage
import allure
from utils.urls import Urls
from utils.locators import YaScooterOrderPageLocator


@allure.story('Тестирование страницы оформления заказа')
class TestYaScooterOrderPage:
    @allure.description('Некорректное Имя')
    def test_order_page_first_name_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_order_page.input_first_name('Вqw')
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_FIRST_NAME_MESSAGE).is_displayed()

    @allure.description('Некорректная Фамилия')
    def test_order_page_last_name_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_order_page.input_last_name('Вqw')
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_LAST_NAME_MESSAGE).is_displayed()

    @allure.description('Некорректный адрес')
    def test_order_page_address_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_order_page.input_address('Вqw')
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_ADDRESS_MESSAGE).is_displayed()

    @allure.description('Не заполнено метро')
    def test_order_page_subway_input_empty_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_SUBWAY_MESSAGE).is_displayed()

    @allure.description('Некорректный номер телефона')
    def test_order_page_telephone_number_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_order_page.input_telephone_number('Вqw')
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_TELEPHONE_NUMBER_MESSAGE).is_displayed()

    @allure.description('Переход на страницу с выбором самоката')
    def test_order_page_go_to_choose_scooter_user_data_correct_open_order_params(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_order_page.input_first_name('Владим')
        ya_scooter_order_page.input_last_name('Владим')
        ya_scooter_order_page.input_address('Миусская')
        ya_scooter_order_page.choose_subway('Беговая')
        ya_scooter_order_page.input_telephone_number('71111111111')
        ya_scooter_order_page.go_next()
        assert len(ya_scooter_order_page.find_elements(YaScooterOrderPageLocator.ORDER_BUTTON)) > 0



