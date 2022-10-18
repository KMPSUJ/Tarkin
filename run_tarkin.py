from Tarkin import Tarkin
import discord
import os

if __name__ == '__main__':
    permissions_path = os.getenv("TARKIN_PERMS")
    token = os.getenv("TARKIN_TOKEN")
    if permissions_path is None:
        print("Bot permissions file not set. Set TARKIN_PERMS environment variable.")
        exit(1)
    if token is None:
        print("Bot token not set. Set TARKIN_TOKEN environment variable.")
        exit(1)

    bot_intents = discord.Intents.default()
    bot_intents.message_content = True
    client = Tarkin(permissions_path, intents=bot_intents)
    client.run(token)
