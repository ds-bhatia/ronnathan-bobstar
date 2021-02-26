import discord
from discord.ext import commands, tasks
import youtube_dl

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name = "summon", aliases=["connect"])
    @commands.has_permissions(manage_guild=True)
    async def _summon(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send("You are not connected to a voice channel!")
            return
        
        else:
            channel = ctx.message.author.voice.channel
        
        await channel.connect



def setup(client):
    client.add_cog(Music(client))