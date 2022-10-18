import discord


class MyId:
    """Sends users ID"""

    async def action_myid(self, message: discord.Message, core_message: str) -> None:
        await message.channel.send(f"Your ID is: {message.author.id}")
