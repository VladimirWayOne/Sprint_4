from pages.base_page import BasePage
from utils.locators import YaScooterHomePageLocator as Locators
import allure

class YaScooterHomePage(BasePage):
    @allure.step('Принять куки')
    def click_cookie_accept(self):
        return self.find_element(Locators.COOKIE_ACCEPT_BUTTON).click()

    @allure.step('Нажать на кнопку заказа вверху страницы')
    def click_top_order_button(self):
        return self.find_element(Locators.TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку заказа внизу страницы')
    def click_bottom_order_button(self):
        return self.find_element(Locators.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Перейти на страницу яндекса')
    def click_yandex_button(self):
        return self.find_element(Locators.YANDEX_SITE_BUTTON).click()

    @allure.step('Принять куки')
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(Locators.FAQ_BUTTONS, 10)
        return elems[question_number].click()


