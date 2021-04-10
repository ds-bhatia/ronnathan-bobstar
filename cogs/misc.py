import discord
import typing
from typing import Union
from discord.ext import commands, tasks


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="github", brief="Go to the github repository")
    async def github(self, ctx):
        github_url = "https://github.com/Technoselbow/ronnathan-bobstar"
        embed = discord.Embed(
            title="Click here to go to the Github repo!", url=github_url, color=discord.Color.dark_gray()
        )
        await ctx.send(embed=embed)

    @commands.command(name="invite", brief="Get the invite link to the bot")
    async def invite(self, ctx):
        invite_url = "https://discord.com/api/oauth2/authorize?client_id=813836773758992404&permissions=0&scope=bot"
        embed = discord.Embed(
            title="Click here to invite Ronnathan Bobstar!", url=invite_url, color=discord.Color.dark_gray())
        await ctx.send(embed=embed)

    @commands.command(name="support", brief="Get the link for the support server")
    async def support(self, ctx):
        await ctx.send("Support Server:\nhttps://discord.gg/EThRPErsQF")

    @commands.command(name="reddit", brief="Get the links for the jojo subreddits")
    async def reddit(self, ctx):
        invite_url = "https://www.reddit.com/r/StardustCrusaders/"
        embed = discord.Embed(
            title="Click here to go to the jojo subreddit!", url=invite_url, color=discord.Color.dark_gray())
        await ctx.send(embed=embed)
        invite_url2 = "https://www.reddit.com/r/ShitpostCrusaders/"
        embed = discord.Embed(
            title="Click here to go to the jojo meme subreddit!", url=invite_url2, color=discord.Color.dark_gray())
        await ctx.send(embed=embed)

    @commands.command(name="killerqueen", breif="Deletes the person's messages", aliases=["kq"])
    @commands.has_guild_permissions(manage_messages = True)
    async def killerqueen(self, ctx, user: Union[discord.Member, int]):
        if user == None:
            await ctx.send("Specify a person smh....")
        if not isinstance(user, int):
            if ctx.author.top_role_position <= user.top_role_position and ctx.guild.owner.id != ctx.author.id:
                await ctx.send("Become more powerful to use the command on this person!")
                return

        if isinstance(user, int):
            user_str = f"<@{user}>"
            user = discord.Object(id=user)

        else:
            user_str = user

        target = user

        if ctx.author.bot:
            return

        elif ctx.author.id == user.id:
            await ctx.delete()

        await ctx.send("you have been cursed owo")


def setup(client):
    client.add_cog(Misc(client))
