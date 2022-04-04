import discord
import os
import requests
import json

import discord.ext
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def dadlink(ctx, id: int):
  await ctx.send(f"https://opensea.io/assets/0xecdd2f733bd20e56865750ebce33f17da0bee461/{id}")
  return

@client.command()
async def momlink(ctx, id: int):
  await ctx.send(f"https://opensea.io/assets/0xecdd2f733bd20e56865750ebce33f17da0bee461/{id}")
  return

@client.command()
async def dad(ctx, id: int):
  await ctx.send(f"https://bafybeia63b5uwzf5ipqcgicy3vujv6ak7czf7juej6mte775p6un7ergri.ipfs.dweb.link/{id}.png")
  return

@client.command()
async def mom(ctx, id: int):
  await ctx.send(f"https://bafybeiao53abkdfpkdtrtxdumt3vn3al6q3cnb7hyzjnqep4milymr6kgi.ipfs.dweb.link/{id}.png")
  return

client.run(os.getenv('TOKEN'))