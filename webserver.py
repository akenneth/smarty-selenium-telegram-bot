import logging
import os

import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.locks
import tornado.options
import tornado.web
from telegram.ext import Updater

from fetchers.base_fetcher import BaseSeleniumFetcher

from handlers.daily_handler import NotificationsHandler

PORT = os.environ.get('WEBSERVER_PORT') or 8888
COOKIE_SECRET = os.environ.get('COOKIE_SECRET') or 'secret'
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/run/(.*)", NotificationsHandler),
        ]
        settings = dict(
            xsrf_cookies=True,
            cookie_secret=COOKIE_SECRET,
            debug=True,
            updater=Updater(token=TELEGRAM_BOT_TOKEN, use_context=True),
            chat_id=CHAT_ID
        )
        super().__init__(handlers, **settings)


async def main():
    app = Application()
    app.listen(PORT)

    logging.info(f"Tornado running with port {PORT}, Chat id: {CHAT_ID}")
    shutdown_event = tornado.locks.Event()
    await shutdown_event.wait()
    BaseSeleniumFetcher.driver.close()


if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)