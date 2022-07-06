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



async def ping(ctx):
    await ctx.send('テストぉ')


async def en(ctx):
    text = tr.translate(message.content, src="en", dest="ja").text
    await ctx.send(text)

@bot.command()
async def text(ctx):
    await ctx.send('**音楽botについて**')
    await ctx.send('🟥基本コマンドの説明\n\n"m!join" -音楽botをVCに入れます\n"m!play" -リンクの動画再生\n"m!skip" -再生中の動画をスキップします\n"m!leave" -VCからbotを蹴ります\n"m!setup" -botの設定\n"m!loop" -音楽のループ再生\n\n\n🟥コマンドの使い方\n\n例)\nm!play https://youtu.be/xxxxxx')
    


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
