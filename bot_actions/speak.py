import discord
from discord.ext import commands
import os


class Speak(commands.Cog):
    """Speak message loudly"""

    async def action_speak(self, message: discord.Message, core_message: str) -> None:
        os.system(f"espeak -s100 -a100 -v pl -k40 '{core_message.lstrip()}'")
        await message.channel.send(f"Message spoken: {core_message.lstrip()}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Speak())
