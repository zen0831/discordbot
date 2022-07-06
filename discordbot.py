from discord.ext import commands
from os import getenv
import traceback
import discord
from discord_buttons_plugin import *
import requests


bot = commands.Bot(command_prefix='/')
buttons = ButtonsClient(bot)



@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@buttons.click
@commands.has_permissions(manage_channels=True, manage_roles=True) 
  async def button_a(ctx, *, nom_de_salon):
      await ctx.reply('こんにちは！🐶')

      guild = ctx.guild
      role = nom_de_salon
      autorize_role = await guild.create_role(name=role)
      overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        autorize_role: discord.PermissionOverwrite(read_messages=True)
      }
      await guild.create_text_channel(nom_de_salon,overwrites=overwrites)
      await ctx.author.add_roles(autorize_role)

@buttons.click
  async def button_b(ctx):
    await ctx.reply("このメッセージはあなたにしか見えていません！", flags = MessageFlags().EPHEMERAL)
    await ctx.reply("5秒後にチャンネルを閉じます")
    time.sleep(5)
    await ctx.channel.purge()


@bot.command()
async def text(ctx):
    await ctx.channel.send('**音楽botについて**')
    await ctx.channel.send('🟥基本コマンドの説明\n\n"m!join" -音楽botをVCに入れます\n"m!play" -リンクの動画再生\n"m!skip" -再生中の動画をスキップします\n"m!leave" -VCからbotを蹴ります\n"m!setup" -botの設定\n"m!loop" -音楽のループ再生\n\n\n🟥コマンドの使い方\n\n例)\nm!play https://youtu.be/xxxxxx')
    
  async def command(ctx):
    await buttons.send(
        content='テストコマンドだよ',
        channel=ctx.channel.id,
        components=[
            ActionRow([
                Button(
                    label='チャンネル作成',
                    style=ButtonType().Primary,
                    custom_id='button_a'
                )
            ]),ActionRow([
                Button(
                    label='テスト',
                    style=ButtonType().Danger,
                    custom_id='button_b'
                )
            ])
        ]
    )

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)