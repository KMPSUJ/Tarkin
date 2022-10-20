import discord
import os

class Speak:
    """Speak message loudly"""

    async def action_speak(self, message: discord.Message, core_message: str) -> None:
        os.system(f"espeak -s100 -a100 -v pl -k40 '{core_message.lstrip()}'")
        await message.channel.send(f"Message spoken: {core_message.lstrip()}")
