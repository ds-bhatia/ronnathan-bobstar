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
        
        if not voice.is_connected():
            await channel.connect()
        else:
            await ctx.send("I am already in a voice channel!")

    @commands.command(name='leave', aliases=["disconnect"])
    async def leave(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if not voice_client.is_connected():
            await ctx.send("I am not connected to a voice channel!")

        else:
            await voice_client.disconnect()

    @commands.command(name="play")
    async def play(ctx, url : str):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)


def setup(client):
    client.add_cog(Music(client))