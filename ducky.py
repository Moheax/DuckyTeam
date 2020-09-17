import discord
import os
import importlib
import logging
#from inspect import getmembers, isfunction
#from utils.db import db
from collections import Counter 
import datetime
from discord.ext.commands import AutoShardedBot as Bot

def get_prefix_callable(defaults):
  def callable(bot, msg):
    prefixes = ['{}'.format(bot.user.mention), '<@!{}>'.format(bot.user.id)]

    if msg.guild:
      try:
        server = db.servers.find_one({ "_id": str(msg.guild.id) })
        if server:
          for pf in server["prefixes"]:
            prefixes.append(pf)
      except:
        pass
    return defaults + prefixes

  return callable

class DuckyClient(Bot): # This doesn't work... The extra prefixes don't get added.
  def __init__(self, *args, **kwargs):
    callable = get_prefix_callable(kwargs["default_prefixes"])

    super().__init__(command_prefix=callable)

    #self.db = db
    self.counter = Counter ()
    self.uptime = datetime.datetime.now()
    self.logger = logging.getLogger('ducky')
    self.default_cogs = kwargs["default_cogs"]

  def init_cogs(self):
    all_cogs = ['cogs.' + os.path.splitext(x)[0] for x in os.listdir('./cogs') if x.endswith('.py')]
    defaults = [x for x in all_cogs if x.split('.')[1] in self.default_cogs]

    total = 0
    for cog in defaults:
      self.load_extension(cog)
      total += 1

    print('Started {}/{} Default Cogs'.format(total, len(defaults)))

  async def launch(self, token):
    self.init_cogs()
    await self.start(token)
