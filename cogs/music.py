import discord
from discord.ext import commands, tasks
import youtube_dl
from discord.voice_client import VoiceClient

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    youtube_dl.utils.bug_reports_message = lambda: ''

    @commands.command(name = "summon", aliases=["play"])
    async def play(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send("You are not connected to a voice channel!")
            return
        
        else:
            channel = ctx.message.author.voice.channel
        
        await channel.connect()

    @commands.command(name='leave', aliases=["disconnect"])
    async def leave(self, ctx):
        if not voice_client.is_connected():
            await ctx.send("I am not connected to a voice channel!")

        else:
            voice_client = ctx.message.guild.voice_client
            await voice_client.disconnect()



def setup(client):
    client.add_cog(Music(client))