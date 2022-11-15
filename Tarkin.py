import discord
import discord.ext.commands as commands
from core.permisions_manager import PermissionsManager
from core.command_functions_manager import CommandFunctionManager
from bot_actions.all import BotActions
from core.CmdManager import CmdManager
import asyncio
import json


class Tarkin(commands.Bot, PermissionsManager, CommandFunctionManager, BotActions):
    """
    Final class for the discord bot.
    """
    bot_greeting: str
    perms: CmdManager

    def __init__(self, config_file: str, *, intents: discord.Intents, **client_options) -> None:
        self.bot_greeting = "Tarkin,"
        commands.Bot.__init__(self, self.bot_greeting, intents=intents, **client_options)

        with open(config_file, "r") as f:
            conf = json.load(f)
        self.load_all_extensions(conf["extensions"])
        self.perms = CmdManager(conf, self)

    def load_all_extensions(self, ext_list: list) -> None:
        for e in ext_list:
            asyncio.run(self.load_extension(e))

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
                if self.perms.check_permissions(message, key):
                    # perform wanted action
                    await self.perms.get_command_function(key)(message,
                                                               message.content.removeprefix(
                                                                   f"{self.bot_greeting} {key}"))
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
