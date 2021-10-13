import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random
# other files with commands



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

@bot.command(name='Goose', help='the geese are unstoppable, they shall be the end of all things.')
async def goose(ctx, message):
    goose_num = random.randint(25, 2048)

    response = (f'Alas, the Geese have taken another victim. {message.author.ping} has been obliterated by {goose_num} Geese! Will not some brave hero come forth, and cause the Geese to Cease?')
    await ctx.send(response)



bot.run(TOKEN)
