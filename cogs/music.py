import discord
from discord.ext import commands, tasks
import youtube_dl
from discord.voice_client import VoiceClient

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    youtube_dl.utils.bug_reports_message = lambda: ''
    

    @commands.command(name = "awaken", aliases=["summon"], brief = "Get the bot to join your voice channel")
    async def play(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send("You are not connected to a voice channel!")
            return
        
        else:
            channel = ctx.message.author.voice.channel
        
        await channel.connect()

    @commands.command(name='arrivederci', aliases=["disconnect"], brief = "Get the bot to leave the voice channel")
    async def leave(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if not voice_client.is_connected():
            await ctx.send("I am not connected to a voice channel!")

        else:
            await voice_client.disconnect()

    @cat.command(pass_context=True)
    async def play(self, ctx, url : str):
        channel = ctx.message.author.voice.channel

def setup(client):
    client.add_cog(Music(client))