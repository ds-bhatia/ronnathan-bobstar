import discord
from discord.ext import commands, tasks
import os

token = os.environ["TOKEN"]

client = commands.Bot(command_prefix = "j!")


@client.command(name = "ora")
async def ora(ctx):
    await ctx.send("ORA ORA ORA ORA ORA!")

@client.command(name = "muda")
async def muda(ctx):
    await ctx.send("MUDA MUDA MUDA MUDA MUDA!")

@client.command(name = "dora")
async def dora(ctx):
    await ctx.send("DORA DORA DORA DORA DORA!")
    
@client.command(name = "arri")
async def arri(ctx):
    await ctx.send("ARRI ARRI ARRI ARRI ARRIVEDERCI!")

client.run(token)
