import logging

from tornado.web import RequestHandler

from fetchers.base_fetcher import BaseSeleniumFetcher
from local import config


class HomeHandler(RequestHandler):
    # expecting 'key/title' -> lambda bot, chat_id, title: ...
    fetch_actions = config.fetch_actions

    async def get(self):
        bot = self.settings.get('updater').bot
        chat_id = self.settings.get('chat_id')
        bot.send_sticker(chat_id=chat_id, sticker='CAACAgIAAxkBAAPqX2UNj7lpxN5zkwFDXvZy318bHxoAAlgEAALO2OgLbPcZZLyyHAYbBA')
        for title, action in HomeHandler.fetch_actions.items():
            logging.info(f'Running action {title}')
            try:
                action(bot, chat_id, title)
            except Exception as err:
                # self.driver.refresh()
                logging.info(f'Action failed, restarting driver: {err}')
                logging.exception(err)
                BaseSeleniumFetcher.close()
                BaseSeleniumFetcher.init_driver()
        self.write("Ok!")
