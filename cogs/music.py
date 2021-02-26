import discord
from discord.ext import commands, tasks
import youtube_dl
from discord.voice_client import VoiceClient

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    youtube_dl.utils.bug_reports_message = lambda: 

    @commands.command(name = "summon", aliases=["play"])
    async def play(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send("You are not connected to a voice channel!")
            return
        
        else:
            channel = ctx.message.author.voice.channel
        
        await channel.connect



def setup(client):
    client.add_cog(Music(client))