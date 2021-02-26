import discord
from discord.ext import commands, tasks
import youtube_dl

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name = "summon", aliases=["connect"])
    @commands.has_permissions(manage_guild=True)
    async def _summon(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):
        if not channel and not ctx.author.voice:
            raise VoiceError('You are neither connected to a voice channel nor specified a channel to join.')
        destination = channel or ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()


def setup(client):
    client.add_cog(Music(client))