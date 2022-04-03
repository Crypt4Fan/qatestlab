from setuptools import find_packages, setup


setup(
    name='qalabtest',
    version='1.0.0',
    description='QA Lab test task',
    packages=find_packages(include=['qalabtest', 'qalabtest.*']),
    python_requires=">=3.8, <4",
    install_requires = [
        'async-generator==1.10',
        'attrs==21.4.0',
        'certifi==2021.10.8',
        'cffi==1.15.0',
        'cryptography==36.0.2',
        'h11==0.13.0',
        'idna==3.3',
        'iniconfig==1.1.1',
        'outcome==1.1.0',
        'packaging==21.3',
        'pluggy==1.0.0',
        'py==1.11.0',
        'pycparser==2.21',
        'pyOpenSSL==22.0.0',
        'pyparsing==3.0.7',
        'PySocks==1.7.1',
        'pytest==7.1.1',
        'selenium==4.1.3',
        'sniffio==1.2.0',
        'sortedcontainers==2.4.0',
        'tomli==2.0.1',
        'trio==0.20.0',
        'trio-websocket==0.9.2',
        'urllib3==1.26.9',
        'wsproto==1.1.0',
    ]
)
