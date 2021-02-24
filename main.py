import discord
from discord.ext import commands, tasks
import os

token = os.environ["TOKEN"]

client = commands.Bot(command_prefix = "j!")

@client.command(name = "ora")
async def ora(self, ctx):
    await ctx.send("ORA ORA ORA ORA ORA!")


client.run(token)
