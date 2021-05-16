import os
import DiscordBot
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv('settings.env')
    TOKEN = os.getenv('TOKEN')
    bot = DiscordBot
    bot.run(TOKEN)
