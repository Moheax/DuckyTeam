import discord
from discord.ext import commands

class troll(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def secret(self, ctx):

		embed=discord.Embed(color=discord.Colour(0xb3d4fc))
		embed.set_image(url="https://media.discordapp.net/attachments/610153897977446401/755889132030656512/Screenshot_20200827-130145.png?width=338&height=702")
		await ctx.send(embed=embed)

def setup(bot):
	c = troll(bot) 
	bot.add_cog(c)