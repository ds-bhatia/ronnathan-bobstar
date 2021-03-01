import discord
from discord.ext import commands, tasks
import youtube_dl
from discord.voice_client import VoiceClient

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    youtube_dl.utils.bug_reports_message = lambda: ''

    @commands.command(name = "awaken", aliases=["summon"])
    async def play(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send("You are not connected to a voice channel!")
            return
        
        else:
            channel = ctx.message.author.voice.channel
        
        await channel.connect()

    @commands.command(name='arrivederci', aliases=["disconnect"])
    async def leave(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if not voice_client.is_connected():
            await ctx.send("I am not connected to a voice channel!")

        else:
            await voice_client.disconnect()



def setup(client):
    client.add_cog(Music(client))