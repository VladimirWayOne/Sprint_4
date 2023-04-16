import time

from pages.home_page import YaScooterHomePage
import allure
from utils.urls import Urls
from utils.locators import YandexPageLocator, YaScooterHomePageLocator, YaScooterOrderPageLocator
from utils.test_data import YaScooterHomePageFAQ



@allure.story('Тестирование перехода на страницу Заказать')
class TestYaScooterHomePage:
    @allure.step('Нажатие на верхнюю кнопку заказа')
    def test_click_top_order_button_show_order_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_top_order_button()
        #ya_scooter_home_page.find_element(YaScooterOrderPageLocator.NEXT_BUTTON)
        assert ya_scooter_home_page.current_url() == Urls.ORDER_PAGE

    @allure.step('Нажатие на нижнюю кнопку заказа')
    def test_click_bottom_order_button_show_order_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_bottom_order_button()

        assert ya_scooter_home_page.current_url() == Urls.ORDER_PAGE

    @allure.step('Перейти на страницу Яндекса/Дзена')
    def test_click_yandex_button_go_to_yandex(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_yandex_button()
        ya_scooter_home_page.switch_window(1)
        ya_scooter_home_page.wait_url_until_not_about_blank()
        current_url = ya_scooter_home_page.current_url()

        assert (Urls.YANDEX_HOME_PAGE in current_url) or (Urls.DZEN_HOME_PAGE in current_url)

    @allure.step('Отобразить ответ на первый вопрос')
    def test_faq_click_first_question_show_answer(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_faq_question(question_number=0)
        answer = ya_scooter_home_page.find_element(YaScooterHomePageLocator.FAQ_ANSWER(0))

        assert answer.is_displayed() and answer.text == YaScooterHomePageFAQ.answer1

