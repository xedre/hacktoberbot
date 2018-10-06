from pathlib import Path
from sys import stderr
from traceback import print_exc
from os import environ
import logging

from discord.ext import commands


class Hacktoberbot(commands.Bot):
    HACKTOBERBOT_TOKEN = environ.get('HACKTOBERBOT_TOKEN')

    def load_cogs(self):
        # Scan for files in the /cogs/ directory and make a list of the file names.
        cogs = [file.stem for file in Path('cogs').glob('*.py')]
        for extension in cogs:
            try:
                bot.load_extension(f'cogs.{extension}')
            except Exception as e:
                logging.critical(f'Failed to load extension {extension}.')
                print_exc()

    def startup(self):
        logging.info("Connecting")
        self.run(self.HACKTOBERBOT_TOKEN)

    def __init__(self, command_prefix, formatter=None, description=None, pm_help=False, **options):
        logging.info("Initialising")
        super(Hacktoberbot, self).__init__(command_prefix=command_prefix, formatter=formatter,
                                           description=description, pm_help=pm_help, options=options)


if __name__ == '__main__':
    bot = Hacktoberbot(command_prefix=commands.when_mentioned_or('!'))
    bot.load_cogs()
    bot.startup()
