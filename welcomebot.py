import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = ".")
@client.event
async def on_ready():
	print("Thank you for using video bot")
	await client.change_presence(game=discord.Game(name=videos"))

@client.event
async def on_message(message):
	if message.content.startswith('.hello'):
		msg = 'Hello (0.author.mention) how are you today'.format(message)
		awiat client.send_message(message.channel, msg)
	if message.content.startswith('.bye'):
		msg = 'Goodbye (0.author.mention) hope to see you again soon :wave:'.format(message)
		awiat client.send_message(message.channel, msg)

client.run(os.getenv('TOKEN'))
