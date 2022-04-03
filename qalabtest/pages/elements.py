from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from qalabtest.pages.base_page import BasePage


class BaseElement():
    def __init__(self, page: BasePage, locator: Tuple[str, str], timeout: int = None):
        self.page = page
        self.locator = locator
        self.driver: WebDriver = page.driver
        self.timeout = timeout or page.setup.timeout


class Button(BaseElement):
    def click(self):
        button: WebElement = WebDriverWait(self.driver, self.timeout).until(
            ec.element_to_be_clickable(self.locator)
        )
        button.click()


class Field(BaseElement):
    def send_keys(self, string: str):
        field: WebElement = WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(self.locator)
        )
        field.clear()
        field.send_keys(string)


class CustomSelect(BaseElement):
    VALUE = (By.XPATH, '//div[@data-test-id="select-value:{}"]')

    def select(self, value: str):
        select: WebElement = WebDriverWait(self.driver, self.timeout).until(
            ec.element_to_be_clickable(self.locator)
        )
        select.click()

        locator = (
            CustomSelect.VALUE[0],
            CustomSelect.VALUE[1].format(value)
        )
        choice: WebElement = WebDriverWait(self.driver, self.timeout).until(
             ec.element_to_be_clickable(locator)
        )
        choice.click()


class Span(BaseElement):
    @property
    def text(self):
        span: WebElement = WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(self.locator)
        )
        return span.text
