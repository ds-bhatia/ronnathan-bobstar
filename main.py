import discord
from discord.ext import commands, tasks
import os
import youtube_dl

token = os.environ["TOKEN"]

client = commands.Bot(command_prefix = "j!", help_command = None)

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
    
@client.command()
async def help(ctx, args=None):
    help_embed = discord.Embed(title="My Bot's Help!")
    command_names_list = [x.name for x in bot.commands]

    # If there are no arguments, just list the commands:
    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(bot.commands)]),
            inline=False
        )
        help_embed.add_field(
            name="Details",
            value="Type `.help <command name>` for more details about each command.",
            inline=False
        )

    # If the argument is a command, get the help text from that command:
    elif args in command_names_list:
        help_embed.add_field(
            name=args,
            value=bot.get_command(args).help
        )


#Import cog

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"{filename} has loaded.")

client.run(token)
