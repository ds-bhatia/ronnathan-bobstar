import discord 
from discord.ext import commands

class Cries(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command(name = "ora")
    async def ora(ctx):
        await ctx.send("ORA ORA ORA ORA ORA!")

    @commands.command(name = "muda")
    async def muda(ctx):
        await ctx.send("MUDA MUDA MUDA MUDA MUDA!")

    @commands.command(name = "dora")
    async def dora(ctx):
        await ctx.send("DORA DORA DORA DORA DORA!")
    
    @commands.command(name = "arri")
    async def arri(ctx):
        await ctx.send("ARRI ARRI ARRI ARRI ARRIVEDERCI!")

def setup(client):
    client.add_cog(Cries(client))