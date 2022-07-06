from discord.ext import commands
from os import getenv
import traceback
from googletrans import Translator
from discord_buttons_plugin import *
import requests




tr = Translator()
bot = commands.Bot(command_prefix='/')
buttons = ButtonsClient(bot)



@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    result = tr.translate(error_msg, src="en", dest="ja").text
    await ctx.send(result)


@bot.command()
async def ping(ctx):
    await ctx.send('テストぉ')

@buttons.click
  async def button_hello(ctx):
    await ctx.reply("こんにちは！")

@buttons.click
  async def button_ephemeral(ctx):
    await ctx.reply("このメッセージはあなたにしか見えていません！", flags = MessageFlags().EPHEMERAL)
    
@bot.command()
  async def create(ctx):
    await buttons.send(
    		content = "テストボタン", 
    		channel = ctx.channel.id,
    		components = [
    			ActionRow([
    				Button(
    					label="Hello", 
    					style=ButtonType().Primary, 
    					custom_id="button_hello"
    				)
    			]),ActionRow([
    				Button(
    					label="Ephemeral",
    					style=ButtonType().Danger,
    					custom_id="button_ephemeral"
    				)
    			])
    		]
    	)


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
