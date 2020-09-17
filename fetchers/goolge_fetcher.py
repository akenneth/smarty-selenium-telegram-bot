import io
import logging
import string
from typing import Any

from fetchers.base_fetcher import BaseSeleniumFetcher


class GoogleFetcher(BaseSeleniumFetcher):
    def fetch_google_card(self, bot: Any, chat_id: int, title: string, url: string, card_id: string) \
            -> (string, io.BytesIO):
        self.driver.get(url)

        self.driver.implicitly_wait(50)
        # cookie accept
        try:
            self.driver.switch_to.frame(0)
            el = self.driver.find_element_by_xpath('//*[@id="introAgreeButton"]')
            el.click()

        except Exception as err:
            logging.info(f'Set cookie failed with {err}')

        self.driver.implicitly_wait(7)
        self.driver.switch_to.default_content()
        ship_class = self.driver.find_element_by_css_selector(f"[id^='{card_id}']")
        element_text = ship_class.text
        img = ship_class.screenshot_as_png
        image_io = io.BytesIO(img)

        bot.send_message(chat_id=chat_id, text=title)
        bot.send_photo(chat_id=chat_id, photo=image_io)
        return element_text, image_io


# Local testing
# g = GoogleFetcher()
# t, io = g.fetch_google_card(None, 0, 't', 'https://www.google.com/search?client=firefox-b-d&q=msft', 'c')
# print(t)
