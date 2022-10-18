import discord
from core.permisions_manager import PermissionsManager
from core.command_functions_manager import CommandFunctionManager
from bot_actions.all import BotActions


class Tarkin(discord.Client, PermissionsManager, CommandFunctionManager, BotActions):
    """
    Final class for the discord bot.
    """
    bot_greeting: str

    def __init__(self, permissions_path: str, *, intents: discord.Intents, **client_options) -> None:
        self.bot_greeting = "Tarkin,"
        self.load_permissions(permissions_path)
        self.load_command_function_names(self.get_command_names())
        discord.Client.__init__(self, intents=intents, **client_options)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: discord.Message) -> None:
        # prevent self response
        if message.author == self.user:
            return
        # check if the bot should react
        if not message.content.startswith(self.bot_greeting):
            return
        # find wanted command, check permissions, and execute it (or inform why not)
        for key in self.get_command_names():
            if message.content.startswith(f"{self.bot_greeting} {key}"):
                # check permissions
                if self.check_permissions(message, key):
                    # perform wanted action
                    self.get_command_function(key)(self, message,
                                                   message.content.removeprefix(f"{self.bot_greeting} {key}"))
                else:
                    await self.wrong_permissins(message)
                return
            else:
                continue
        # if no command found
        await self.unknown_command(message)

    async def unknown_command(self, message: discord.Message) -> None:
        # IMPLEMENT !!!!!!!!!!!!!!!!!!!!
        await message.channel.send("Unknown command.")
        print("Unknown command")
        return

    async def wrong_permissins(self, message: discord.Message) -> None:
        # IMPLEMENT !!!!!!!!!!!!!!!!!!!!
        await message.channel.send("Wrong permissions.")
        print("Wrong permissions")
        return


if __name__ == '__main__':
    perm_path = "example_permissions.json"
    bot_intents = discord.Intents.default()
    bot_intents.message_content = True

    client = Tarkin(perm_path, intents=bot_intents)
