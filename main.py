from ducky import duckyclient
import asyncio

if __name__ == '__main__':
    TOKEN = ''
    PREFIXES = ['!']
    COGS = ['general']

    bot = duckyclient(default_prefixes = PREFIXES, default_cogs = COGS)


    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.launch(TOKEN))
