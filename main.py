import discord
from discord.ext import commands, tasks
import os
import youtube_dl
from pretty_help import PrettyHelp

token = os.environ["TOKEN"]

client = commands.Bot(command_prefix = "j!", help_command=PrettyHelp())

@client.command(name = "github")
async def github(ctx):
    github_url = "https://github.com/Technoselbow/ronnathan-bobstar"
    embed = discord.Embed(
        title = "Click here to go to the Github repo!", url = github_url, color = discord.Color.dark_gray()
    )
    await ctx.send(embed = embed)

@client.command(name = "invite")
async def invite(ctx):
    invite_url = "https://discord.com/api/oauth2/authorize?client_id=813836773758992404&permissions=0&scope=bot"
    embed = discord.Embed(
        title = "Click here to invite Ronnathan Bobstar!", url = invite_url, color = discord.Color.dark_gray())
    await ctx.send(embed = embed)

@client.command(name = "support")
async def support(ctx):
    await ctx.send("Support Server:\nhttps://discord.gg/EThRPErsQF")

@client.command(name = "reddit")
async def reddit(ctx):
    invite_url = "https://www.reddit.com/r/StardustCrusaders/"
    embed = discord.Embed(
        title = "Click here to go to the jojo subreddit!", url = invite_url, color = discord.Color.dark_gray())
    await ctx.send(embed = embed)
    invite_url2 = "https://www.reddit.com/r/ShitpostCrusaders/"
    embed = discord.Embed(
        title = "Click here to go to the jojo meme subreddit!", url = invite_url2, color = discord.Color.dark_gray())
    await ctx.send(embed = embed)
    


#Import cog

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"{filename} has loaded.")

client.run(token)
