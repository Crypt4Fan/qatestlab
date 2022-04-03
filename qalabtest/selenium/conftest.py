import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service

from qalabtest.configuration import BaseConfig, ProdConfig


@pytest.fixture(scope='session')
def config():
    # Фикстуру можно расширить для чтения нужного конфига в 
    # зависимости от опции командной строки
    return ProdConfig()


@pytest.fixture()
def driver(config: BaseConfig):
    service = Service(executable_path=config.chrome_driver_path)
    options = ChromeOptions()
    options.add_argument('--start-maximized')
    driver = Chrome(service=service, options=options)
    yield driver
    driver.close()


class TestSetup():
    def __init__(self, **kwargs) -> None:
        for attr, value in kwargs.items():
            setattr(self, attr, value)


@pytest.fixture
def test_setup(config: BaseConfig, driver: pytest.fixture) -> TestSetup:
    return TestSetup(**{
        'driver': driver,
        'email': config.email,
        'pwd': config.pwd,
        'timeout': config.timeout
    })
