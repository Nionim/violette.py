# sys
import config
# Other
import disnake, aiohttp, logging, datetime, os
from disnake.ext import commands

now = datetime.datetime.now()
time = now.strftime("%H:%M:%S")
#logging.basicConfig(filename='./logs/discord.log', encoding='utf-8', level=logging.INFO)
#logging.info(f"\n\n{'-' * 25}(Stardet on {time} {now.day}.{now.month}){'-' * 25}\n")

class Violette(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix = config.PROFILE["prefix"],
            owner_ids = config.PROFILE["owner_ids"],
            status=config.PROFILE["status"],

            allowed_mentions=disnake.AllowedMentions.none(),
            intents=disnake.Intents.all(),
            help_command=None,

            activity=disnake.Activity(
                type=disnake.ActivityType.custom,
                name=config.PROFILE["activity_name"],
                state=config.PROFILE["activity_state"]
            )
        )
        self.session = aiohttp.ClientSession(loop=self.loop)

def init_dirs():
    dirs = ["./logs", "./cogs"]

    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)

if __name__ == "__main__":
    init_dirs()

    bot = Violette()

    bot.load_extensions("cogs")
    bot.run(config.TOKEN)