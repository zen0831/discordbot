from discord.ext import commands
from os import getenv
import traceback
from googletrans import Translator

tr = Translator()
bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    result = tr.translate(error_msg, src="en", dest="ja").text

    await ctx.send(result)


@bot.command()
async def ping(ctx):
    await ctx.send('テストぉ')


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
