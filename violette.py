# sys
import config
# Other
import disnake, aiohttp, logging, datetime, os
from disnake.ext import commands

def init_dirs():
    dirs = ["./logs", "./cogs"]

    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)

now = datetime.datetime.now()
time = now.strftime("%H:%M:%S")


init_dirs()
logging.basicConfig(filename='./logs/discord.log', encoding='utf-8', level=logging.INFO)
logging.info(f"\n\n{'-' * 25}(Started on {time} {now.day}.{now.month}){'-' * 25}\n")

class Violette(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix=config.PROFILE["prefix"],
            owner_ids=config.PROFILE["owner_ids"],
            test_guilds=config.PROFILE["test_guilds"],
            status=config.PROFILE["status"],

            allowed_mentions=disnake.AllowedMentions.none(),
            intents=disnake.Intents.all(),
            help_command=None,

            activity=disnake.Activity(
                type=config.PROFILE["activity_type"],
                name=config.PROFILE["activity_name"],
                state=config.PROFILE["activity_state"]
            )
        )
        self.session = aiohttp.ClientSession(loop=self.loop)

async def on_disconnect(self):
    await self.session.close()
    await super().close()

if __name__ == "__main__":
    bot = Violette()

    shards_count: int = bot.shards.keys().__len__()

    if shards_count == 1:
        bot.shards[0].reconnect()
        print(f"Zero shard reconnected")

    bot.load_extensions("cogs")
    bot.run(config.TOKEN)