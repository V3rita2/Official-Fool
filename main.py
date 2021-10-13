import os
import discord
from dotenv import load_dotenv
import random


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to discord')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    greet_options = [
        "hello",
        "greetings, human",
        "IM ASSBELLS MCGEE GIMME YOUR TEETH",
    ]

    if message.content == 'greet the fool':
        response = random.choice(greet_options)
        await message.channel.send(response)

client.run(TOKEN)