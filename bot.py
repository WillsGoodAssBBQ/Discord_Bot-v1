import random
import asyncio
import aiohttp
import discord
import platform
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands


  
BOT_PREFIX = ("-")
TOKEN = "NDExOTU3MzczNzMzODMwNjU3.DdmqGQ.XZrRHMU4BPxhBO2FOorhVTH_WqQ"  # Get at discordapp.com/developers/applications/me


bot = commands.Bot(command_prefix=BOT_PREFIX)
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    return await client.change_presence(game=discord.Game(name='William Is Da Best Fam!')) #This is buggy, let us know if it doesn't work.
            
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))



#async def list_servers():
    #await client.wait_until_ready()
    #while not client.is_closed:
        #print("Current servers:")
        #for server in client.servers:
            #print(server.name)
        #await asyncio.sleep(600)
        

@client.command(name='hello',
                description="says hello",
                brief="hello",
                aliases=['hi','hia','hey'],
                pass_context=True)
async def hello(context):
    possible_responses = [
        'Hello',
        'Hia',
        'Wag wan!'
        ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name='info',
                description="info",
                brief="info",
                aliases=[],
                pass_context=True)
async def info(context):
    embed = discord.Embed(title="WillsGoodAssBot", description="Version 1.0", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="WillsGoodAssBBQ#6692")
    
    # Shows the number of servers the bot is member of.
    #embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="https://discord.gg/9gPDFSZ")
    await client.say(embed=embed)

client.remove_command('help')

@client.command(name='help',
             description="help",
             pass_context=True)
async def help(context):
    embed = discord.Embed(title="WillsGoodAssBot", description="Version 1.0", color=0xeee657)

    embed.add_field(name="hello", value="Gives a nice greet message", inline=False)
    embed.add_field(name="square", value="Squares a number", inline=False)
    embed.add_field(name="8ball", value="Follow the command with a yes/no question", inline=False)
    embed.add_field(name="clear", value="Follow with a value to delete messages {Max 100, 14days or under} +secret{s}   Owner Only!", inline=False)
    #embed.add_field(name="help", value="Gives this message", inline=False)
    embed.add_field(name="help", value="Gives this message", inline=False)
    await client.say(embed=embed)

@client.command(pass_context = True)
@commands.has_role("CEO")
async def spurge(ctx, number):
    number = int(number) #Converting the amount of messages to delete to an integer
    counter = 0
    async for x in client.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await client.delete_message(x)
            counter += 1
            await asyncio.sleep(1.2)
            
@client.command(pass_context = True)
@commands.has_role("CEO") # checks and sees if user has the role CEO
async def purge(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
		 


    
#client.loop.create_task(list_servers())
client.run(TOKEN)

