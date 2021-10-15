import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random
# other files with commands



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix= ['F!', 'f!'])

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord')

# a simple little hello
@bot.command(name='hello', help='says hello in a very friendly manner and most certainly doesnt ask for your teeth')
async def hello(ctx):

    greet_options = [
        "hello",
        "greetings, human",
        "IM ASSBELLS MCGEE GIMME YOUR TEETH",
    ]

    response = random.choice(greet_options)
    await ctx.send(response)
# copys what is said after the command
@bot.command(name='copycat', help='Replication of input')
async def copycat(ctx, *, message):
    await ctx.send(f'you said: {message}')
   
# this command will use embeds and pictures when I figure them out
@bot.command(name='tarot', aliases=['Tarot', 'tatot'], help='draws a tarot card for you to answer a question. Only has Major arcana currently because I\'m lazy')
async def tarot(ctx, *, query):
    cards = [
        'The Fool',
        'The Magician',
        'The High Priestess',
        'The Empress',
        'The Hierophant',
        'The Lovers',
        'The Chariot',
        'Strength',
        'The Hermit',
        'Wheel of Fortune',
        'Justice',
        'The Hanged Man',
        'Death',
        'Temperance',
        'The Devil',
        'The Tower',
        'The Star',
        'The Moon',
        'The Sun',
        'Judgement',
        'The World',
    ]

    if query == 'can i beat the shit out of you without getting closer?':
        choice = 'The World'
    else:
        choice = random.choice(cards)

    if choice == 'The World':
        await ctx.send(f'{choice} is the answer to {query}.\n This means It Was Me, DIO!')
    else:
        await ctx.send(f'{choice} is the answer to {query}.\n I will tell you what this means once my brain is finished.')



# clear command
@bot.command()
async def clear (ctx, amount=1):
    await ctx.channel.purge(limit=amount)

#little kick command for fun
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

# we fuck around and find out
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

# we unfuck
@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)


bot.run(TOKEN)
