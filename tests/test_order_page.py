import pytest

from pages.order_page import YaScooterOrderPage
import allure
from utils.urls import Urls
from utils.locators import YaScooterOrderPageLocator
from utils.test_data import YaScooterOrderPageData as order_data


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

    @allure.description('Заполнить данные на этапе "Для кого самокат" и перейти на этап "Про аренду"')
    def test_order_page_go_to_choose_scooter_user_data_correct_open_about_rent(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_order_page.fill_user_data(order_data.data_sets['data_set1'])
        ya_scooter_order_page.go_next()
        assert len(ya_scooter_order_page.find_elements(YaScooterOrderPageLocator.ORDER_BUTTON)) > 0

    @allure.description('Заполнить данные на этапе "Про аренду" и оформить заказ')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_about_rent_input_correct_data_and_order_show_order_number(self, driver, data_set):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_order_page.fill_user_data(order_data.data_sets[data_set])
        ya_scooter_order_page.go_next()
        ya_scooter_order_page.fill_rent_data(order_data.data_sets[data_set])
        ya_scooter_order_page.click_order()
        ya_scooter_order_page.click_accept_order()
        assert len(ya_scooter_order_page.find_elements(YaScooterOrderPageLocator.ORDER_COMPLETED_INFO)) > 0

    @allure.description('Заполнить данные на этапе "Про аренду", оформить заказ и перейти на статус заказа')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_create_order_and_go_order_status(self, driver, data_set):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_order_page.fill_user_data(order_data.data_sets[data_set])
        ya_scooter_order_page.go_next()
        ya_scooter_order_page.fill_rent_data(order_data.data_sets[data_set])
        ya_scooter_order_page.click_order()
        ya_scooter_order_page.click_accept_order()
        order_number = ya_scooter_order_page.get_order_number()
        ya_scooter_order_page.click_go_to_status()
        current_url = ya_scooter_order_page.current_url()
        assert (Urls.ORDER_STATUS_PAGE in current_url) and (order_number in current_url)




