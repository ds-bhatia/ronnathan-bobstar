import discord
from discord.ext import commands, tasks

token = os.environ("TOKEN")

client = commands.Bot(command_prefix = "j!")

client.run(token)
