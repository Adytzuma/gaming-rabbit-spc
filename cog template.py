import discord
from discord.ext import commands


class Cog:
    def __init__(self, client):
        self.client = client






    @commands.command()
    async def hello(self):
        await bot.say('oh hi')












def setup(client):
        client.add_cog(Cog(client))
