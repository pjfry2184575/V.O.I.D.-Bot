from guilded.ext import commands

from commands.faction.faction_info import faction_info
from config import Bot_Token

bot = commands.Bot(command_prefix='!') 

@bot.event
async def on_ready() -> None:
  print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
  await ctx.send('Pong!')

@bot.command()
async def balance(ctx):
  await ctx.send('I don\'t know! I\'m a bot!')

@bot.command()
async def faction(ctx):
  await faction_info(ctx)

bot.run(Bot_Token)