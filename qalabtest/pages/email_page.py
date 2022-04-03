from selenium.webdriver.common.by import By

from qalabtest.pages.elements import Button, Field, Span
from .base_page import BasePage

class EmailPage(BasePage):
    URL = 'https://e.mail.ru/inbox'

    USERNAME_SPAN = (By.XPATH, '//span[@class="ph-project__user-name svelte-1hiqrvn"]')
    WRITE_EMAIL_BUTTON = (By.XPATH, '//span[@class="compose-button__txt"]')
    TO_INPUT = (By.XPATH, '//div[@data-type="to"]//input')
    SUBJECT_INPUT = (By.XPATH, '//div[@class="compose-app__compose"]//input[@name="Subject"]')
    BODY_INPUT = (By.XPATH, '//div[@class="compose-app__compose"]//div[@role="textbox"]')
    SEND_EMAIL_BUTTON = (By.XPATH, '//span[@class="button2__txt"]')

    @property
    def current_user(self):
        span = Span(self, EmailPage.USERNAME_SPAN)
        return span.text

    def click_write_email_button(self):
        button = Button(self, EmailPage.WRITE_EMAIL_BUTTON)
        button.click()
        return self

    def fill_to_field(self, email: str):
        field = Field(self, EmailPage.TO_INPUT)
        field.send_keys(email)
        return self

    def fill_subject_field(self, subject: str):
        field = Field(self, EmailPage.SUBJECT_INPUT)
        field.send_keys(subject)
        return self

    def fill_body(self, body: str):
        field = Field(self, EmailPage.BODY_INPUT)
        field.send_keys(body)
        return self

    def click_send_email_button(self):
        button = Button(self, EmailPage.SEND_EMAIL_BUTTON)
        button.click()
        return self
