#!/usr/bin/python3.7

import discord
import time
from os import environ


client = discord.Client()
voice = None

@client.event
async def on_ready():
    print(f"Herro {client.user.name}")
    print(f"Opus support: {discord.opus.is_loaded()}")


async def join_channel(message):
    global voice
    if not voice:
      channel =  message.author.voice.channel
      if channel:
          voice = await channel.connect(reconnect=True)
          source = discord.FFmpegPCMAudio("./musklex.mp3")
          voice.play(source)
          while voice.is_playing():
              time.sleep(1)
          await voice.disconnect()
          voice = None

@client.event
async def on_message(message):
    if message.content == f"musklex":
        await join_channel(message)


client.run(environ.get("TOKEN"))
