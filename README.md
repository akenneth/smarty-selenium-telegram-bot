# smarty-selenium-telegram-bot
Capturing screenshots with selenium and sending results to telegram

## This project consists of:
- A python tornado webserver, that runs the different selenium jobs on a call to '/'
- A kubernetes cronjob worker configuration to call the tornado service.

## Setup:
- Build the docker image
- Run with -port and set the env variables 
- Curl localhost:port and check your telegram chat for results!

- If running in kubernetes, see cronjob deploy for example of using a cronjob worker to fire the jobs
```
docker build . -t smarty:v0.5 
docker run -p 8887:8888 -e TELEGRAM_BOT_TOKEN="your-token" -e TELEGRAM_CHAT_ID="your chat id" smarty:v0.5
curl localhost:8887
```

Note: TELEGRAM_CHAT_ID is your chat id with your configured telegram bot. You can get it by running the telegram_bot script, starting a chat with your bot and sending '/start' to it. The chat id will be printed to console.
See: telegram_bot.py script or [Telegram bot intro](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot)

## Adding your own fetchers
- Create your selenium fetchers, see google_fetcher.py for example
- Add use of that fetchers by modifying the dict at handler.py

## Other notes:
This is an initial stage project, still fails sometimes etc. Overall works surprisingly well :) 