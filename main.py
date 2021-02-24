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

@client.command(name = "invite")
async def invite(ctx):
    invite_url = "https://discord.com/api/oauth2/authorize?client_id=813836773758992404&permissions=0&scope=bot"
    embed = discord.Embed(
        title = "Click here to invite Ronnathan Bobstar!", url = invite_url, color = discord.Color.dark_gray())
    await ctx.send(embed = embed)

@client.command(name = "support")
async def support(ctx):
    await ctx.send("Support Server:\nhttps://discord.gg/EThRPErsQF")

client.run(token)
