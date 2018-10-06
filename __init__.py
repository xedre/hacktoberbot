import logging
import os
import sys
import bot.bot
from logging import handlers
from discord.ext import commands

logging_handlers = [logging.StreamHandler(stream=sys.stderr),
                    handlers.TimedRotatingFileHandler("logs/log.txt", when="s", interval=5, utc=True)]

logging.basicConfig(
    format="%(asctime)s Bot: | %(name)30s | %(levelname)8s | %(message)s",
    datefmt="%b %d %H:%M:%S",
    handlers=logging_handlers
)


hackbot = bot.bot.Hacktoberbot(command_prefix=commands.when_mentioned_or('!'))
hackbot.load_cogs()
hackbot.startup()

logging.info("Closing down")
logging.shutdown()
