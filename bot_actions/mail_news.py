import discord
from discord.ext import commands
from DiscordPermBot.permbot import PermBot
from tempfile import mktemp
import os


class MailNews(commands.Cog):
    """Sends news to a mailing list through mutt"""
    bot: commands.Bot
    chanel: int
    mail: str
    header: str
    footer: str

    def __init__(self, bot: PermBot):
        self.bot = bot
        self.chanel = int(bot.config["MailNews"]["chanel"])
        self.mail = bot.config["MailNews"]["mail"]
        self.header = bot.config["MailNews"]["header"]
        self.footer = bot.config["MailNews"]["footer"]

    async def action_send_by_mail(self, message: discord.Message, core_message: str) -> None:
        if message.channel.id != self.chanel:
            return

        tmp_file_name = mktemp()
        with open(tmp_file_name, "w") as f:
            f.write(self.header)
            f.write("\n\n")
            f.write(core_message)
            f.write("\n\n")
            f.write(self.footer)
            f.write("\n")

        os.system(f"mutt -s 'SMP News' '{self.mail}' < '{tmp_file_name}'")


async def setup(bot: PermBot):
    await bot.add_cog(MailNews(bot))
