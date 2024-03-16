# <center>Telegram Match Notifier Bot<center>

## Introduction

This documentation provides information about Telegram-Match-Notifier-Bot, a telegram bot designed to inform users about ongoing match statuses retrieved from an API. Telegram-Match-Notifier-Bot retrieves data from the API and notifies users whether the match is currently at halftime or has reached fulltime.You can access the match notifier bot via https://t.me/result_notification_bot

---

## Features

- Integration with API-FOOTBALL: The bot utilizes the API-FOOTBALL to fetch real-time match data.
- https://rapidapi.com/api-sports/api/api-football
- https://www.api-football.com/

---

## Getting Started

1. Installation: Clone the repository from GitHub:

```bash
git clone https://github.com/anitdevrim/Telegram-Match-Notifier-Bot
```

2. Configuration: Add a .env file into directory. Your .env file should look like this.

```bash
TOKEN = ''
BOT_USERNAME = ''
API_KEY = ''
hostname = ''
database = ''
username = ''
pwd = ''
port_id = ''
```

Make sure that .env file is on the main directory.

3. Run the application

```bash
docker-compose up --build
```

---

## Usage

Users can find the telegram bot by searching [@result_notification_bot](https://t.me/result_notification_bot) in Telegram. After starting the chat use /commands to see all the commands that can be used.

### Commands

- /start : Start the bot and get a welcome message.
- /help : Get an information about what bot can do.
- /commands : View all the commands that can be used.
- /set team_name : Add a team to your follow list.
- /listteams : View all the teams that you added to your follow list.
- /deleteteam team_name : Delete a team that is in your follow list.
- /deleteall : Delete all the teams that are in your follow list.
