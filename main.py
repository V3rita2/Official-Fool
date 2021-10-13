import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random
import 


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix= '@.@')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord')


@bot.command(name='hello', help='says hello in a very friendly manner and most certainly doesnt ask for your teeth')
async def hello(ctx):

    greet_options = [
        "hello",
        "greetings, human",
        "IM ASSBELLS MCGEE GIMME YOUR TEETH",
    ]

    response = random.choice(greet_options)
    await ctx.send(response)

bot.run(TOKEN)