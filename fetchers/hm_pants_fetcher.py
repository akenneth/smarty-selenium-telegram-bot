import io
import logging
import string
from typing import Any

from selenium.webdriver import ActionChains
from telegram.ext import Updater

from fetchers.base_fetcher import BaseSeleniumFetcher


class HMPantsFetcher(BaseSeleniumFetcher):
    def fetch_package_status(self, bot: Any, chat_id: int, title: string, url: string) -> (string, io.BytesIO):
        self.small_driver.get(url)
        self.small_driver.implicitly_wait(20)
        # self.try_accept_pop_up()
        # self.small_driver.refresh()
        # self.small_driver.implicitly_wait(30)

        # click 'choose size'
        self.try_accept_pop_up()
        self.small_driver.refresh()
        search_el = self.wait_for_element_in_view(lambda: self.small_driver.find_element_by_class_name("trigger-button"))
        self.small_driver.execute_script("arguments[0].scrollIntoView();", search_el)
        search_el.click()

        # choose 's'
        s_el = self.wait_for_element_in_view(lambda: self.small_driver.find_element_by_class_name(
            'picker-list'))
        # s_el = self.wait_for_element_in_view(lambda: self.small_driver.find_element_by_css_selector(
        #     'li[data-code="0525500001002"]'))
        # self.small_driver.execute_script("arguments[0].scrollIntoView();", s_el)
        # s_el.click()

        ship_class = s_el
        # ship_class = self.wait_for_element_in_view(lambda: self.small_driver.find_element_by_css_selector('div.inner:nth-child(1)'))
        element_text = ship_class.text
        print(element_text)
        img = ship_class.screenshot_as_png
        image_io = io.BytesIO(img)

        bot.send_message(chat_id=chat_id, text=title)
        bot.send_photo(chat_id=chat_id, photo=image_io)
        return element_text, image_io

    def try_accept_pop_up(self):
        try:
            el = self.wait_for_element_in_view(lambda: self.small_driver.find_element_by_css_selector('button.close:nth-child(2)'))

            if not el.is_displayed():
                raise Exception("Element cookie is not in view")
            el.click()

        except Exception as err:
            # self.small_driver.refresh()
            logging.info(f'Set cookie failed with {err}')
            print(err)

    def wait_for_element_in_view(self, f):
        count = 0
        el = f()
        while count < 10 and not el.is_displayed():
            logging.info(f'wait_for_element_in_view: waiting for el to be in view')
            el = f()
            count += 1
            self.small_driver.implicitly_wait(20)
        if not el.is_displayed():
            logging.info(f'wait_for_element_in_view: timed out, el not in view')
        return el


