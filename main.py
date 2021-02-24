import discord
from discord.ext import commands, tasks
import os

token = os.environ["TOKEN"]

client = commands.Bot(command_prefix = "j!")

@client.command(name = "invite")
async def invite(ctx):
    invite_url = "https://discord.com/api/oauth2/authorize?client_id=813836773758992404&permissions=0&scope=bot"
    embed = discord.Embed(
        title = "Click here to invite Ronnathan Bobstar!", url = invite_url, color = discord.Color.dark_gray())
    await ctx.send(embed = embed)

@client.command(name = "support")
async def support(ctx):
    await ctx.send("Support Server:\nhttps://discord.gg/EThRPErsQF")

#Import cog

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"{filename} has loaded.")

client.run(token)
