# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:11:02 2018

@author: Amrita
"""

import telegram
from telegram.ext import Updater, CommandHandler
import logging
import pickle
import matplotlib.pyplot as plt






### Set up the bot.
# If you want to use this bot yourself, please message me directly.
token = open('ignore/token.txt', 'r').read()
bot = telegram.Bot(token=token)

# Create an updater to fetch updates.
updater = Updater(token=token)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -'
                    '%(message)s', level=logging.INFO)