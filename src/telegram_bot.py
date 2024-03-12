import os
from datetime import datetime

from dotenv import load_dotenv
from telegram import Bot
from telegram.ext import *
from unidecode import unidecode

from src.db_manager import Table

load_dotenv()

TOKEN = os.getenv("TOKEN")

table = Table()
time_sent = datetime.now()
formatted_time_sent = time_sent.strftime('%Y-%m-%d %H:%M:%S')

class TelegramBot():
    def __init__(self):
        self.application = Application.builder().token(TOKEN).build()
        self.setup_handlers()
        self.bot = Bot(token=TOKEN)
    
    def setup_handlers(self):
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CommandHandler('set', self.set))
        self.application.add_handler(CommandHandler('help', self.help))
        self.application.add_handler(CommandHandler('commands', self.commands))
        self.application.add_handler(CommandHandler('deleteteam',self.deleteteam))
        self.application.add_handler(CommandHandler('deleteall',self.deleteall))
        self.application.add_handler(CommandHandler('listteams',self.listteams))
    
    def run(self):
        self.application.run_polling(1.0)
    
    async def send_message_to_user(self,user_id, message):
        try:
            await self.bot.send_message(chat_id = user_id, text=message)
            print("Message sent succesfully!")
            table.insert_into_info_table(user_id,message,formatted_time_sent)
        except Exception as e:
            print(f"Failed to send message: {e}")

    async def start(self, update, context):
        await update.message.reply_text("Hello! You can start using the bot! - /commands to show commands!")

    async def set(self,update, context):
        user_id = update.effective_user.id
        args = context.args

        if len(args) == 0:
            await update.message.reply_text("Please provide a team name.")
            return
        team_name = ' '.join(args)
        new_team = unidecode(team_name).title()

        table.insert_table(user_id, new_team)
        await update.message.reply_text(f"{new_team} is added to your list!")

    async def help(self,update, context):
        await update.message.reply_text("This bot gives you the results of the matches you choose!")

    async def commands(self,update, context):
        await update.message.reply_text("""
        /set team_name - Choose the team that you want to follow
/help - Bot information
/deleteteam team_name - Choose the team that you want to unfollow
/deleteall - Unfollow all the teams that you follow
/listteams - List all the teams that you follow
    """)

    async def deleteteam(self,update,context):
        user_id = update.effective_user.id
        team_name = context.args[0]
        new_team = unidecode(team_name).title()
        table.delete_team(user_id,new_team)
        await update.message.reply_text(f"Successfully deleted {new_team} from your list!")

    async def deleteall(self,update,context):
        user_id = update.effective_user.id
        table.delete_all(user_id)
        await update.message.reply_text("Successfully deleted all!")

    async def listteams(self,update,context):
        user_id = update.effective_user.id
        team_list = table.select_from_table(user_id)
        for team in team_list:
            await update.message.reply_text(team)
