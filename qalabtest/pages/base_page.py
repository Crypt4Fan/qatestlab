from qalabtest.selenium.conftest import TestSetup


class BasePage:
    URL: str = None

    def __init__(self, setup: TestSetup):
        self.setup = setup
        self.driver = setup.driver

    def go(self, url: str = None):
        _url = url or self.__class__.URL
        self.driver.get(_url)
        return self
