import discord 
from discord.ext import commands

class Cries(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name = "ora", description = "ORA!")
    async def ora(self, ctx):
        await ctx.send("ORA ORA ORA ORA ORA!")

    @commands.command(name = "muda", description = "MUDA!")
    async def muda(self, ctx):
        await ctx.send("MUDA MUDA MUDA MUDA MUDA!")

    @commands.command(name = "dora", description = "DORA!")
    async def dora(self, ctx):
        await ctx.send("DORARARARARARA!")
    
    @commands.command(name = "arri", description = "ARRIVEDERCI!")
    async def arri(self, ctx):
        await ctx.send("ARRI ARRI ARRI ARRI ARRIVEDERCI!")

def setup(client):
    client.add_cog(Cries(client))