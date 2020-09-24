import io
import logging
import string
from typing import Any

from fetchers.base_fetcher import BaseSeleniumFetcher


class ILPostFetcher(BaseSeleniumFetcher):
    def fetch_package_status(self, bot: Any, chat_id: int, title: string, url: string) -> (string, io.BytesIO):
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        # cookie accept
        self.try_accept_pop_up()

        # click 'search'
        search_el = self.driver.find_element_by_id("btn-ItemCode")
        search_el.click()
        self.driver.implicitly_wait(15)
        self.try_accept_pop_up()
        ship_class = self.driver.find_element_by_id('result')
        element_text = ship_class.text
        img = ship_class.screenshot_as_png
        image_io = io.BytesIO(img)

        bot.send_message(chat_id=chat_id, text=title)
        bot.send_photo(chat_id=chat_id, photo=image_io)
        return element_text, image_io

    def try_accept_pop_up(self):
        try:
            el = self.driver.find_element_by_css_selector('img[alt="סגור"]')
            el.click()

        except Exception as err:
            logging.info(f'Set cookie failed with {err}')


# Local testing
# g = ILPostFetcher()
# t, io = g.fetch_package_status(None, 0, 't', 'https://mypost.israelpost.co.il/itemtrace/?OpenForm&L=EN&itemcode=CY285043013DE')
# print(t)