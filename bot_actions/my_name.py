import discord


class MyName:
    """Sends users ID"""

    async def action_myname(self, message: discord.Message, core_message: str) -> None:
        await message.channel.send(f"Your name is: {message.author.name}")
