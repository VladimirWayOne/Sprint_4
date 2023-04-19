import time

from pages.order_page import YaScooterOrderPage
import allure
from utils.urls import Urls
from utils.locators import YaScooterOrderPageLocator




@allure.story('Тестирование перехода на страницу Заказать')
class TestYaScooterOrderPage:
    def test_order_page_first_name_input_correct(self, driver):
        ya_scooter_home_page = YaScooterOrderPage(driver)
        ya_scooter_home_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page.input_first_name('Вдадимир')


