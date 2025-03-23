import telebot
from ..api.apis import bot_api
import re

spotify_link_pattern = re.compile(r'https://open\.spotify\.com')

bot = telebot.TeleBot(bot_api, parse_mode=None) 
