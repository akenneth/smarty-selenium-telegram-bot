# smarty-selenium-telegram-bot
Capturing screenshots with selenium and sending results to telegram

## This project consists of:
- A python tornado webserver, that runs the different selenium jobs on a call to '/'
- A kubernetes cronjob worker configuration to call the tornado service.

## Setup:
- Build the docker image
- Run with -port and set the env variables
- Curl localhost:port to check results!

- If running in kubernetes, see cronjob deploy for example of using a cronjob worker to fire the jobs
```
docker build . -t smarty:v0.5 
docker run -p 8887:9999 smarty:v0.5 -e TELEGRAM_BOT_TOKEN="your-token" -e TELEGRAM_CHAT_ID="your chat id"
curl localhost:8887
```

## Adding your own fetchers
- Create your selenium fetchers, see google_fetcher.py for exanple
- Add use of that fetchers by modifying the dict at handler.py

## Other notes:
This is an initial stage project, still fails sometimes etc. Overall works surprisingly well :) 