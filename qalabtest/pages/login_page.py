from selenium.webdriver.common.by import By

from qalabtest.pages.elements import Button, CustomSelect, Field
from .base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://account.mail.ru'

    USER_INPUT = (By.XPATH, '//input[@name="username"]')
    DOMAIN_SELECT = (By.XPATH, '//div[@data-test-id="domain-select"]')
    PASSWORD_BUTTON = (By.XPATH, '//button[@data-test-id="next-button"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@data-test-id="submit-button"]')

    def set_user(self, user: str):
        field = Field(self, LoginPage.USER_INPUT)
        field.send_keys(user)
        return self

    def set_domain(self, domain: str):
        select =CustomSelect(self, LoginPage.DOMAIN_SELECT)
        select.select(domain)
        return self

    def set_email(self, email: str = None):
        _email = email or self.setup.email
        user, domain = _email.split('@')
        return self.set_user(user).set_domain(domain)

    def click_password_button(self):
        button = Button(self, LoginPage.PASSWORD_BUTTON)
        button.click()
        return self

    def set_password(self, pwd: str = None):
        _pwd = pwd or self.setup.pwd
        field = Field(self, LoginPage.PASSWORD_INPUT)
        field.send_keys(_pwd)
        return self

    def submit(self):
        button = Button(self, LoginPage.SUBMIT_BUTTON)
        button.click()
        return self
