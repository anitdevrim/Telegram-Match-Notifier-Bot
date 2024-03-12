import asyncio
import json
from datetime import datetime

from src.db_manager import Table
from src.telegram_bot import TelegramBot


class MatchNotifier:
    def __init__(self):
        with open('data.json') as f:
            self.data = json.load(f)
        self.table = Table()
        self.bot = TelegramBot()

        self.previous_statuses = {}

    def notify_matches(self):
        current_date = datetime.now()
        formatted_date = current_date.strftime('%H:%M:%S')
        users = self.table.select_distinct_user() # All users
        for user in users:
            teams = self.table.select_from_table(user)
            for team in teams:
                for match in self.data['response']:
                    home_team = match['teams']['home']['name']
                    away_team = match['teams']['away']['name']
                    status = match['fixture']['status']['short']
                    match_id = match['fixture']['id']
                    
                    if team == home_team or team == away_team:
                        previous_status = self.previous_statuses.get(user, {}).get(match_id)
                        print(f"Previous status: {previous_status}")
                        print(f"Current status: {status}")
                        if previous_status != status:
                            self.previous_statuses.setdefault(user, {})[match_id] = status
                            if status == 'HT':
                                halftime_score = f"{match['score']['halftime']['home']} - {match['score']['halftime']['away']}"
                                message = f"Halftime: {home_team} vs {away_team}. Score: {halftime_score}"
                                asyncio.run(self.bot.send_message_to_user(user[0], message))
                                print(message)
                                print(formatted_date)
                            elif status == 'FT':
                                fulltime_score = f"{match['score']['fulltime']['home']} - {match['score']['fulltime']['away']}"
                                message = f"Fulltime: {home_team} vs {away_team}. Final score: {fulltime_score}"
                                asyncio.run(self.bot.send_message_to_user(user[0], message))
                                print(message)
                                print(formatted_date)




