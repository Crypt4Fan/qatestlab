class BaseConfig:
    chrome_driver_path: str = ''
    email: str = None
    pwd: str = None
    timeout: int = 10


class ProdConfig(BaseConfig):
    email = ''
    pwd = ''
