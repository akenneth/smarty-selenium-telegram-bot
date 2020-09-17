import io
import logging
import string
from typing import Any

from fetchers.base_fetcher import BaseSeleniumFetcher


class PackageFetcher(BaseSeleniumFetcher):
    def fetch_package_status(self, bot: Any, chat_id: int, title: string, url: string) -> (string, io.BytesIO):
        self.driver.get(url)

        # cookie accept
        try:
            el = self.driver.find_element_by_id("accept-recommended-btn-handler")
            el.click()

        except Exception as err:
            logging.info(f'Set cookie failed with {err}')

        self.driver.implicitly_wait(7)
        ship_class = self.driver.find_element_by_class_name('shipment')
        element_text = ship_class.text
        img = ship_class.screenshot_as_png
        image_io = io.BytesIO(img)

        bot.send_message(chat_id=chat_id, text=title)
        bot.send_photo(chat_id=chat_id, photo=image_io)
        return element_text, image_io
