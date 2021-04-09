import discord
from discord.ext import commands, tasks
import os
import youtube_dl
from pretty_help import PrettyHelp

token = os.environ["TOKEN"]

client = commands.Bot(command_prefix = "j!", help_command=PrettyHelp())

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "JoJo || j!help"))

@client.event
async def on_message(message):
    if message.author.id == 513016113702109185:
        await message.delete()
    else:
        await client.process_commands(message)

# Import cog

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"{filename} has loaded.")

client.run(token)
