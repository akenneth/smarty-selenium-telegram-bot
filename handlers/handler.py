import logging

from tornado.web import RequestHandler

from fetchers.dhl_package_fetcher import PackageFetcher
from fetchers.goolge_fetcher import GoogleFetcher


class HomeHandler(RequestHandler):
    fetch_actions = {       # expecting 'key/title' -> lambda bot, chat_id, title: ...
        'DHl package to IL':
            lambda bot, chat_id, title:
            PackageFetcher().fetch_package_status(bot,
                                                  chat_id,
                                                  title,
                                                  'https://www.dhl.de/de/privatkunden/pakete-empfangen/verfolgen.html?lang=de&idc=Your-package-id),
        'MSFT stock':
            lambda bot, chat_id, title:
            GoogleFetcher().fetch_google_card(bot,
                                              chat_id,
                                              title,
                                              'https://www.google.com/search?client=firefox-b-d&q=msft',
                                              'knowledge-finance-wholepage__entity-summary'),
        '1 Eur in ILS':
            lambda bot, chat_id, title:
            GoogleFetcher().fetch_google_card(bot,
                                              chat_id,
                                              title,
                                              'https://www.google.com/search?client=firefox-b-d&q=1 eur in usd',
                                              'currency-v2')
    }

    async def get(self):
        bot = self.settings.get('updater').bot
        chat_id = self.settings.get('chat_id')
        for title, action in HomeHandler.fetch_actions.items():
            logging.info(f'Running action {title}')
            action(bot, chat_id, title)
        self.write("Ok!")
