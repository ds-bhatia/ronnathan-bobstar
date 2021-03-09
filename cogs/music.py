import discord
from discord.ext import commands, tasks
import youtube_dl
from discord.voice_client import VoiceClient
import os

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    youtube_dl.utils.bug_reports_message = lambda: ''
    

    @commands.command(name = "awaken", aliases=["summon"], brief = "Get the bot to join your voice channel")
    async def awaken(self, ctx):
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

    @commands.command()
    async def play(self, ctx, url : str):
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'stop' command")
            return

        channel = ctx.message.author.voice.channel
        await channel.connect()
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))

def setup(client):
    client.add_cog(Music(client))