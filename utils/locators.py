from selenium.webdriver.common.by import By


class YaScooterHomePageLocator:
    TOP_ORDER_BUTTON = [By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"]
    BOTTOM_ORDER_BUTTON = [By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"]
    FAQ_BUTTONS = [By.XPATH, ".//div[@class='accordion__button']"]
    FAQ_ANSWERS = [By.CSS_SELECTOR, ".accordion__panel > p"]
    ORDER_STATUS_BUTTON = [By.XPATH, ".//button[text()='Статус заказа']"]
    COOKIE_ACCEPT_BUTTON = [By.XPATH, ".//button[text()='да все привыкли']"]
    YANDEX_SITE_BUTTON = [By.XPATH, ".//img[@alt='Yandex']/parent::a"]

    @classmethod
    def FAQ_QUESTION_BUTTON(cls, question_number):
        return [By.XPATH, f".//div[@class='accordion__button' and @id='accordion__heading-{question_number}']"]

    @classmethod
    def FAQ_ANSWER(cls, answer_number):
        return [By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{answer_number}']/p"]


class YaScooterOrderPageLocator:
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]


class YandexPageLocator:
    DOWNLOAD_BUTTON = [By.XPATH, ".//a[text='Установить']"]
    SEARCH_BUTTON = [By.XPATH, ""]
    # DOWNLOAD_BROWSER_BUTTON = [By.XPATH, ""]
