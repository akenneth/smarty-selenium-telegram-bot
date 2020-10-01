import logging

from selenium import webdriver


class BaseSeleniumFetcher:
    driver = None
    small_driver = None

    def __init__(self):
        BaseSeleniumFetcher.init_driver()
        BaseSeleniumFetcher.init_small_driver()

    @classmethod
    def init_driver(cls):
        if cls.driver:
            return

        driver = cls.create_driver(small_mode=False)

        driver.implicitly_wait(10)
        cls.driver = driver

    @classmethod
    def init_small_driver(cls):
        if cls.small_driver:
            return

        driver = cls.create_driver(small_mode=True)

        driver.implicitly_wait(10)
        cls.small_driver = driver

    @classmethod
    def create_driver(cls, small_mode):
        logging.info(f"Web driver init small_mode:{small_mode}")
        options_f = webdriver.FirefoxOptions()
        options_f.headless = True

        if small_mode:
            user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", user_agent)
            driver = webdriver.Firefox(options=options_f, firefox_profile=profile)
            driver.set_window_size(360, 640)
        else:
            driver = webdriver.Firefox(options=options_f)

        return driver

    @classmethod
    def close(cls):
        logging.info("Web driver shutting down")
        if cls.driver:
            cls.driver.quit()

        if cls.small_driver:
            cls.small_driver.quit()
        cls.driver = None
        cls.small_driver = None
