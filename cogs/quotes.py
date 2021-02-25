import discord
from discord.ext import commands, tasks
import random

class Quotes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name = "quote")
    async def quote(self, ctx):
        quotes = [
            "Even Speedwagon is afraid! \n      - Johnathan Joestar",
            "Your next line is...! \n       - Joseph Joestar",
            "WRYYYYYY! \n       - DIO",
            "MUDA MUDA MUDA MUDA MUDAAA! \n     - DIO",
            "OH NO! \n      - Joseph Joestar",
            "Yare, Yare Daze... \n      - Jotaro Kujo"
            "NIGERUNDAYOO! \n       - Jotaro Kujo"
            "There are times when a gentleman has to be courageous and fight, even when his opponent is bigger than he is and he knows he’s going to lose! \n       - Jonathan Joestar"
            "You may have outsmarted me, but I have outsmarted your outsmarting! \n         - Joseph Joestar"

        ]
        await ctx.send(random.choice(quotes))

def setup(client):
    client.add_cog(Quotes(client))