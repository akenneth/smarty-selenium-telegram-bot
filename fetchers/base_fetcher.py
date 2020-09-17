import logging

from selenium import webdriver


class BaseSeleniumFetcher:
    driver = None

    def __init__(self):
        BaseSeleniumFetcher.init_driver()

    @classmethod
    def init_driver(cls):
        if cls.driver:
            return

        logging.info("Web driver init")
        options_f = webdriver.FirefoxOptions()
        options_f.headless = True
        driver = webdriver.Firefox(options=options_f)

        driver.implicitly_wait(10)
        cls.driver = driver

    @classmethod
    def close(cls):
        logging.info("Web driver shutting down")
        cls.driver.quit()
