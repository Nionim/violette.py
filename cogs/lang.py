from disnake.ext import commands
from lib import languagelib
from lib.user_data import VI_USER

class SetLanguage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="lang", description="Set your language")
    async def set_lang(self, inter, language: str = commands.Param(choices=languagelib.LANG_CHOICES)):
        user = VI_USER(inter.author.id)
        user.set_language(language)
        print(f"{inter.author.id} setted lang to {language}")

def setup(bot):
    bot.add_cog(SetLanguage(bot))