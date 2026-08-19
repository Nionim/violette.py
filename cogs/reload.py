from disnake.ext import commands

class BotReload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="reload", description="Reload bot")
    @commands.is_owner()
    async def reload_commands(self, inter):
        await inter.response.defer(ephemeral=True)
        await self.bot.sync_commands()
        await inter.followup.send("reloaded.", ephemeral=True)

def setup(bot):
    bot.add_cog(BotReload(bot))