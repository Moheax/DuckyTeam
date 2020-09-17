import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	print ('logged in as')
	print( bot.user.name)
	prin('---------')

@bot.command()
async def boop(ctx):
	embed=discord.Embed(color=Discord.Colour(0xFFFFFF))
	embed.add_field(name="Boop", value="Yes", inline=false)
	ctx.send(embed=embed)
	
bot.run('')
