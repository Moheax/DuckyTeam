import discord
from discord.ext import commands
import sys
import asyncio
import logging
import os
import importlib
import traceback
import threading
import datetime
import glob
import aiohttp

class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):

        embed = discord.Embed(description = '{}ms'.format(self.bot.latency * 1000), colour=0xb3d4fc)
        await ctx.send(embed=embed)
        
    @commands.command()
	
	async def cogs(self, ctx):
		"""Shows all parts of the bot."""
		modules = [x.replace(".py", "") for x in os.listdir("cogs") if ".py" in x]
		loaded = [c.__module__.split(".")[-1] for c in self.bot.cogs.values()]
		unloaded = [c.split(".")[-1] for c in modules if c.split(".")[-1] not in loaded]
		total_modules = len(modules)
		embed=discord.Embed(title=f"Solyx dashboard | Cogs ({total_modules})", colour=discord.Colour(0xfffffc))
		embed.add_field(name=f"✅ Loaded ({len(loaded)})", value=", ".join(loaded) if loaded != [] else "None", inline=False)
		embed.add_field(name=f"⛔ Unloaded ({len(unloaded)})", value="\n".join(unloaded) if unloaded != [] else "None", inline=False)
		try:
			await ctx.send(embed=embed)
		except:
			try:
				await ctx.send(":pencil2: | Please give me permissions to send embeded messages.")
			except:
				return

	@commands.command()
	
	async def load(self, ctx, *, module: str):
		"""Load a part of the bot."""
		modules = [x.replace(".py", "") for x in os.listdir("cogs") if ".py" in x]
		msg = ""
		if module.lower() == "all":
			for m in modules:
				if not m == "general":
					try:
						self.bot.load_extension("cogs."+m)
						msg += "`{}` ".format(m)
					except Exception as e:
						print(f'{e}')
						pass
			embed=discord.Embed(title="Cogs Loaded", description=msg, colour=0xfffffc)
			try:
				await ctx.send(embed=embed)
			except:
				try:
					await ctx.send(":pencil2: | Please give me permissions to send embeded messages.")
				except:
					return
		else:
			try:
				self.bot.load_extension("cogs."+module)
			except Exception as e:
				print(f'{e}')
				try:
					await ctx.send(":pencil2: | I couldn't load the cog.")
					return
				except Exception as e:
					print(f'{e}')
					return
			embed=discord.Embed(title="Cog Loaded", description="`{}`".format(module), colour=0xfffffc)
			try:
				await ctx.send(embed=embed)
			except:
				try:
					await ctx.send(":pencil2: | Please give me permissions to send embeded messages.")
				except:
					return

	@commands.command()
	
	async def unload(self, ctx, *, module: str):
		"""Unload a part of the bot."""
		modules = [x.replace(".py", "") for x in os.listdir("cogs") if ".py" in x]
		msg = ""
		if module.lower() == "all":
			for m in modules:
				if not m == "general":
					try:
						self.bot.unload_extension("cogs."+m)
						msg += "`{}` ".format(m)
					except Exception as e:
						print(f'{e}')
						pass
			embed=discord.Embed(title="Cogs Unloaded", description=msg, colour=0xfffffc)
			try:
				await ctx.send(embed=embed)
			except:
				try:
					await ctx.send(":pencil2: | Please give me permissions to send embeded messages.")
				except:
					return
		else:
			try:
				self.bot.unload_extension("cogs."+module)
			except Exception as e:
				print(f'{e}')
				try:
					await ctx.send(":pencil2: | I couldn't unload the cog.")
					return
				except:
					return
			embed=discord.Embed(title="Cog Unloaded", description="`{}`".format(module), colour=0xfffffc)
			try:
				await ctx.send(embed=embed)
			except:
				try:
					await ctx.send(":pencil2: | Please give me permissions to send embeded messages.")
				except:
					return

	@commands.command(hidden=True)
	
	async def reload(self, ctx, *, module: str):
		"""Reloads a part of the bot."""
		modules = [x.replace(".py", "") for x in os.listdir("cogs") if ".py" in x]
		msg = ""
		if module.lower() == "all":
			for m in modules:
				if not m == "general":
					try:
						self.bot.reload_extension("cogs."+m)
						msg += "`{}` ".format(m)
					except Exception as e:
						print(f'{e}')
						pass
			embed=discord.Embed(title="Cogs Reloaded", description=msg, colour=0xfffffc)
			try:
				await ctx.send(embed=embed)
			except:
				try:
					await ctx.send(":pencil2: | Please give me permissions to send embeded messages.")
				except:
					return
		else:
			try:
				self.bot.reload_extension("cogs."+module)
			except Exception as e:
				print(f'{e}')
				try:
					await ctx.send(":pencil2: | I couldn't reload the cog.")
					return
				except:
					return
			embed=discord.Embed(title="Cog Reloaded", description="`{}`".format(module), colour=0xfffffc)
			try:
				await ctx.send(embed=embed)
			except:
				try:
					await ctx.send(":pencil2: | Please give me permissions to send embeded messages.")
				except:
					return
def setup(bot):
    c = general(bot) 
    bot.add_cog(c)
