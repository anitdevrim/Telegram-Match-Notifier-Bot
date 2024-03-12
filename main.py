import os
import time

from src.db_manager import Table
from src.get_json import GetJsonFromApi
from src.match_notifier import MatchNotifier
from src.telegram_bot import TelegramBot


def main():
    telegram_bot = TelegramBot()
    match_notifier = MatchNotifier()
    db_manager = Table()
    fetch_api = GetJsonFromApi()

    db_manager.create_user_table()
    db_manager.create_info_table()

    fpid = os.fork()
    if fpid != 0:
        telegram_bot.run()
    
    while True:
        fetch_api.get_json()
        print("JSON FETCHED")
        match_notifier.notify_matches()
        time.sleep(720)

if __name__ == '__main__':
    main()
