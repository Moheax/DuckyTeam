import discord
from discord.ext import commands 

class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):

        embed = discord.Embed(description = '{}ms'.format(self.bot.latency * 1000), colour=0xb3d4fc)
        await ctx.send(embed=embed)

def setup(bot):
    c = general(bot) 
    bot.add_cog(c)
