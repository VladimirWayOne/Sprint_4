from selenium.webdriver.common.by import By


class YaScooterHomePageLocator:
    TOP_ORDER_BUTTON = [By.XPATH, ".//button[text()='Заказать']/parent::div[starts-with(@class, 'Header')]"]
    BOTTOM_ORDER_BUTTON = [By.XPATH, ".//button[text()='Заказать']/parent::div[starts-with(@class, 'Home')]"]
    FAQ_BUTTONS = [By.CSS_SELECTOR, ".accordion__button"]
    FAQ_ANSWERS = [By.CSS_SELECTOR, ".accordion__panel > p"]
    ORDER_STATUS_BUTTON = [By.XPATH, ".//button[text()='Статус заказа']"]