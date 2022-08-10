import os
import collections
import discord
from discord.ext import commands
import requests
from datetime import datetime
import subprocess
import time
import json
import datetime
import random
import string
import pymongo
from discord.ext.commands import has_permissions
from discord.ext.commands import has_role
from discord.ext.commands import cooldown
from discord.ext.commands import BucketType

bot = commands.Bot(command_prefix="-")
bot.remove_command('help')
bot.remove_command('methods')

servers = [986635218029011015]

@bot.command()
@has_role('Mr Man')
async def nuke(ctx):
	await ctx.channel.purge(limit=100000)
	nuke = discord.Embed(title="This Channel Has Been Nuked", color=0x000000)
	nuke.set_image(url="https://bestanimations.com/Military/Explosions/explosion-animated-gif-39.gif")
	nuke.set_footer(text="By Paradym")
	await ctx.send(embed=nuke)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('.gg/Ab6767TCSY | -help By Paradym '))
    print(f'''      
      █████   █    ██  ▄▄▄       ███▄    █ ▄▄▄█████▓ █    ██  ███▄ ▄███▓
    ▒██▓  ██▒ ██  ▓██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒ ██  ▓██▒▓██▒▀█▀ ██▒
    ▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██  ▒██░▓██    ▓██░
    ░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▓▓█  ░██░▒██    ▒██ 
    ░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ▒▒█████▓ ▒██▒   ░██▒
    ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░
    ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░░ ░░   ░ ▒░    ░    ░░▒░ ░ ░ ░  ░      ░
        ░   ░  ░░░ ░ ░   ░   ▒      ░   ░ ░   ░       ░░░ ░ ░ ░      ░   
    ░       ░           ░  ░         ░             ░            ░   
    Gen Bot By Paradym''')
    print('')
    print('    Owner: Paradym')
    print('    Connection:')
    print('    [ESTABLISHED]')
    print('    The Bot Is Now Online')
    print('    ')
    print('    Logs:')

@bot.command()
async def help(ctx):
    if ctx.message.guild.id in servers:
        help = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪", color=0x000000, description="These Are The List Of All Of The Commands")
        ####help.add_field(name="-admin", value="Shows Admin Commands ", inline=False)
        ####help.add_field(name="-funny", value="Funny Shit", inline=False)
        help.add_field(name="-gen", value="Shows Generator Options", inline=False)
        help.add_field(name="-credits", value="Shows Credits", inline=False)
        help.set_footer(text="𝙎𝙚𝙧𝙖𝙥𝙝 Bot By Paradym")
        await ctx.send(embed=help)
        print(f"    {ctx.author} used help in {ctx.channel}")
        channel = bot.get_channel(1006979964299661333)
        log = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙇𝙤𝙜𝙨", color=0x000000)
        log.add_field(name=f"{ctx.author}", value=f"used help in {ctx.channel}", inline=False)
        await channel.send(embed=log)
    else:
        err = discord.Embed(title="Invalid Server ID", color=0x000000, description="")
        err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
        err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
        await ctx.send(embed=err)
        channel = bot.get_channel(1006979964299661333)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log = discord.Embed(title="ATTENTION", color=0x000000, description="")
        log.add_field(name="UNKOWN SERVER ID", value="Someone invited me to a retarded server", inline=False)
        log.add_field(name="Server:", value=f"{ctx.message.guild.id}", inline=False)
        log.add_field(name="Server Invite", value= (link), inline=False)
        await channel.send(embed=log)

##@bot.command()
##@has_role('Mr Man')
##@has_role('Admin')
##async def admin(ctx):
    ##admin = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙋𝙧𝙞𝙘𝙚", color=0x000000)
    ##admin.add_field(name="Bot Access", value="$25 Monthly | Free IP Blacklist | Cooldown 20 Seconds | Funnel : [Comming Soon]", inline=False)
    ##admin.add_field(name="IP Blacklist", value="$10 Lifetime | Get Your IP Blacklisted Off Formonix Bot", inline=False)
    ##admin.set_footer(text="DM One Of The Owners If You Want To Get Reseller!")
    ##await ctx.send(embed=admin)
    ##print(f"    {ctx.author} used admin in {ctx.channel}")
    ##channel = bot.get_channel(1006979964299661333)
    ##log = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙇𝙤𝙜𝙨", color=0x000000)
    ##log.add_field(name=f"{ctx.author}", value=f"used admin in {ctx.channel}", inline=False)
    ##await channel.send(embed=log)


@bot.command()
async def gen(ctx):
    if ctx.message.guild.id in servers:
        gen = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
        gen.add_field(name="-steam", value="Grabs A steam Account", inline=False)
        gen.add_field(name="-roblox", value="Grabs A roblox Account", inline=False)
        gen.add_field(name="-valorant", value="Grabs A valorant Account", inline=False)
        gen.add_field(name="-hbo", value="Grabs A hbo Account", inline=False)
        gen.add_field(name="-disney", value="Grabs A disney+ Account", inline=False)
        gen.add_field(name="-netflix", value="Grabs A netflix Account", inline=False)
        gen.add_field(name="-random", value="Grabs A random email", inline=False)
        await ctx.send(embed=gen)
        print(f"    {ctx.author} used gen in {ctx.channel}")
        channel = bot.get_channel(1006979964299661333)
        log = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙇𝙤𝙜𝙨", color=0x000000)
        log.add_field(name=f"{ctx.author}", value=f"used gen in {ctx.channel}", inline=False)
        await channel.send(embed=log)     
    else:
        err = discord.Embed(title="Invalid Server ID", color=0x000000, description="")
        err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
        err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
        await ctx.send(embed=err)
        channel = bot.get_channel(1006979964299661333)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log = discord.Embed(title="ATTENTION", color=0x000000, description="")
        log.add_field(name="UNKOWN SERVER ID", value="Someone invited me to a retarded server", inline=False)
        log.add_field(name="Server:", value=f"{ctx.message.guild.id}", inline=False)
        log.add_field(name="Server Invite", value= (link), inline=False)
        await channel.send(embed=log)

    
@bot.command()
@commands.cooldown(1,85, commands.BucketType.user)
async def steam(ctx):
    if ctx.message.guild.id in servers:
        with open('steam.txt','r') as txt:
            content = txt.readline()
            gen = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            gen.add_field(name="Account Grabbed", value= (content) , inline=False)
            await ctx.author.send(embed=gen)
            res = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            res.add_field(name="Account Grabbed", value= ("Please check your dms") , inline=False)
            await ctx.send(embed=res)
            print(f"    {ctx.author} has genned a steam account in {ctx.channel}")
            channel = bot.get_channel(1006979964299661333)
            log = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙇𝙤𝙜𝙨", color=0x000000)
            log.add_field(name=f"{ctx.author}", value=f"has genned a steam account in {ctx.channel}", inline=False)
            await channel.send(embed=log)
            cool = discord.Embed(title=f"{ctx.author} your 85 second cooldown has started...", color=0x000000)
            await ctx.send(embed=cool)
            with open("steam.txt", "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != (content):
                        f.write(i)
                    f.truncate()
    else:
        err = discord.Embed(title="Invalid Server ID", color=0x000000, description="")
        err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
        err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
        await ctx.send(embed=err)
        channel = bot.get_channel(1006979964299661333)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log = discord.Embed(title="ATTENTION", color=0x000000, description="")
        log.add_field(name="UNKOWN SERVER ID", value="Someone invited me to a retarded server", inline=False)
        log.add_field(name="Server:", value=f"{ctx.message.guild.id}", inline=False)
        log.add_field(name="Server Invite", value= (link), inline=False)
        await channel.send(embed=log)

@steam.error
async def attack_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"𝙎𝙚𝙧𝙖𝙥𝙝 | 𝘾𝙤𝙤𝙡𝙙𝙤𝙬𝙣",description=f"Jesus wait {error.retry_after:20f} seconds ya greedy cunt.", color=0x000000)
            await ctx.send(embed=em)

@bot.command()
@commands.cooldown(1,85, commands.BucketType.user)
async def netflix(ctx):
    if ctx.message.guild.id in servers:
        with open('net.txt','r') as txt:
            content = txt.readline()
            gen = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            gen.add_field(name="Account Grabbed", value= (content) , inline=False)
            await ctx.author.send(embed=gen)
            res = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            res.add_field(name="Account Grabbed", value= ("Please check your dms") , inline=False)
            await ctx.send(embed=res)
            print(f"    {ctx.author} has genned a netflix account in {ctx.channel}")
            channel = bot.get_channel(1006979964299661333)
            log = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙇𝙤𝙜𝙨", color=0x000000)
            log.add_field(name=f"{ctx.author}", value=f"has genned a netflix account in {ctx.channel}", inline=False)
            await channel.send(embed=log)
            cool = discord.Embed(title=f"{ctx.author} your 85 second cooldown has started...", color=0x000000)
            await ctx.send(embed=cool)
            with open("net.txt", "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != (content):
                        f.write(i)
                    f.truncate()
    else:
        err = discord.Embed(title="Invalid Server ID", color=0x000000, description="")
        err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
        err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
        await ctx.send(embed=err)
        channel = bot.get_channel(1006979964299661333)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log = discord.Embed(title="ATTENTION", color=0x000000, description="")
        log.add_field(name="UNKOWN SERVER ID", value="Someone invited me to a retarded server", inline=False)
        log.add_field(name="Server:", value=f"{ctx.message.guild.id}", inline=False)
        log.add_field(name="Server Invite", value= (link), inline=False)
        await channel.send(embed=log)

@netflix.error
async def attack_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"𝙎𝙚𝙧𝙖𝙥𝙝 | 𝘾𝙤𝙤𝙡𝙙𝙤𝙬𝙣",description=f"Jesus wait {error.retry_after:20f} seconds ya greedy cunt.", color=0x000000)
            await ctx.send(embed=em)

@bot.command()
@commands.cooldown(1,85, commands.BucketType.user)
async def roblox(ctx):
    if ctx.message.guild.id in servers:
        with open('roblox.txt','r') as txt:
            content= txt.readline()
            gen = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            gen.add_field(name="Account Grabbed", value= (content) , inline=False)
            await ctx.author.send(embed=gen)
            res = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            res.add_field(name="Account Grabbed", value= ("Please check your dms") , inline=False)
            await ctx.send(embed=res)
            print(f"    {ctx.author} has genned a roblox account in {ctx.channel}")
            channel = bot.get_channel(1006979964299661333)
            log = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙇𝙤𝙜𝙨", color=0x000000)
            log.add_field(name=f"{ctx.author}", value=f"has genned a roblox account in {ctx.channel}", inline=False)
            await channel.send(embed=log)
            cool = discord.Embed(title=f"{ctx.author} your 85 second cooldown has started...", color=0x000000)
            await ctx.send(embed=cool)
            with open("roblox.txt", "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != (content):
                        f.write(i)
                    f.truncate()
    else:
        err = discord.Embed(title="Invalid Server ID", color=0x000000, description="")
        err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
        err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
        await ctx.send(embed=err)
        channel = bot.get_channel(1006979964299661333)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log = discord.Embed(title="ATTENTION", color=0x000000, description="")
        log.add_field(name="UNKOWN SERVER ID", value="Someone invited me to a retarded server", inline=False)
        log.add_field(name="Server:", value=f"{ctx.message.guild.id}", inline=False)
        log.add_field(name="Server Invite", value= (link), inline=False)
        await channel.send(embed=log)

@roblox.error
async def attack_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"𝙎𝙚𝙧𝙖𝙥𝙝 | 𝘾𝙤𝙤𝙡𝙙𝙤𝙬𝙣",description=f"Jesus wait {error.retry_after:20f} seconds ya greedy cunt.", color=0x000000)
            await ctx.send(embed=em)

@bot.command()
@commands.cooldown(1,85, commands.BucketType.user)
async def valorant(ctx):
    if ctx.message.guild.id in servers:
        with open('val.txt','r') as txt:
            content= txt.readline()
            gen = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            gen.add_field(name="Account Grabbed", value= (content) , inline=False)
            await ctx.author.send(embed=gen)
            res = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            res.add_field(name="Account Grabbed", value= ("Please check your dms") , inline=False)
            await ctx.send(embed=res)
            print(f"    {ctx.author} has genned a valorant account in {ctx.channel}")
            channel = bot.get_channel(1006979964299661333)
            log = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙇𝙤𝙜𝙨", color=0x000000)
            log.add_field(name=f"{ctx.author}", value=f"has genned a valorant account in {ctx.channel}", inline=False)
            await channel.send(embed=log)
            cool = discord.Embed(title=f"{ctx.author} your 85 second cooldown has started...", color=0x000000)
            await ctx.send(embed=cool)
            with open("val.txt", "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != (content):
                        f.write(i)
                    f.truncate()
    else:
        err = discord.Embed(title="Invalid Server ID", color=0x000000, description="")
        err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
        err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
        await ctx.send(embed=err)
        channel = bot.get_channel(1006979964299661333)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log = discord.Embed(title="ATTENTION", color=0x000000, description="")
        log.add_field(name="UNKOWN SERVER ID", value="Someone invited me to a retarded server", inline=False)
        log.add_field(name="Server:", value=f"{ctx.message.guild.id}", inline=False)
        log.add_field(name="Server Invite", value= (link), inline=False)
        await channel.send(embed=log)
    
@valorant.error
async def attack_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"𝙎𝙚𝙧𝙖𝙥𝙝 | 𝘾𝙤𝙤𝙡𝙙𝙤𝙬𝙣",description=f"Jesus wait {error.retry_after:20f} seconds ya greedy cunt.", color=0x000000)
            await ctx.send(embed=em)

@bot.command()
@commands.cooldown(1,85, commands.BucketType.user)
async def hbo(ctx):
    if ctx.message.guild.id in servers:
        with open('hbo.txt','r') as txt:
            content= txt.readline()
            gen = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            gen.add_field(name="Account Grabbed", value= (content) , inline=False)
            await ctx.author.send(embed=gen)
            res = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            res.add_field(name="Account Grabbed", value= ("Please check your dms") , inline=False)
            await ctx.send(embed=res)
            print(f"    {ctx.author} has genned a hbo account in {ctx.channel}")
            channel = bot.get_channel(1006979964299661333)
            log = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙇𝙤𝙜𝙨", color=0x000000)
            log.add_field(name=f"{ctx.author}", value=f"has genned a hbo account in {ctx.channel}", inline=False)
            await channel.send(embed=log)
            cool = discord.Embed(title=f"{ctx.author} your 85 second cooldown has started...", color=0x000000)
            await ctx.send(embed=cool)
            with open("hbo.txt", "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != (content):
                        f.write(i)
                    f.truncate()
    else:
        err = discord.Embed(title="Invalid Server ID", color=0x000000, description="")
        err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
        err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
        await ctx.send(embed=err)
        channel = bot.get_channel(1006979964299661333)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log = discord.Embed(title="ATTENTION", color=0x000000, description="")
        log.add_field(name="UNKOWN SERVER ID", value="Someone invited me to a retarded server", inline=False)
        log.add_field(name="Server:", value=f"{ctx.message.guild.id}", inline=False)
        log.add_field(name="Server Invite", value= (link), inline=False)
        await channel.send(embed=log)
    
@hbo.error
async def attack_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"𝙎𝙚𝙧𝙖𝙥𝙝 | 𝘾𝙤𝙤𝙡𝙙𝙤𝙬𝙣",description=f"Jesus wait {error.retry_after:20f} seconds ya greedy cunt.", color=0x000000)
            await ctx.send(embed=em)

@bot.command()
@commands.cooldown(1,85, commands.BucketType.user)
async def random(ctx):
    if ctx.message.guild.id in servers:
        with open('rando.txt','r') as txt:
            content= txt.readline()
            gen = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            gen.add_field(name="Account Grabbed", value= (content) , inline=False)
            await ctx.author.send(embed=gen)
            res = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            res.add_field(name="Account Grabbed", value= ("Please check your dms") , inline=False)
            await ctx.send(embed=res)
            print(f"    {ctx.author} has genned a random account in {ctx.channel}")
            channel = bot.get_channel(1006979964299661333)
            log = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙇𝙤𝙜𝙨", color=0x000000)
            log.add_field(name=f"{ctx.author}", value=f"has genned a random account in {ctx.channel}", inline=False)
            await channel.send(embed=log)
            cool = discord.Embed(title=f"{ctx.author} your 85 second cooldown has started...", color=0x000000)
            await ctx.send(embed=cool)
            with open("rando.txt", "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != (content):
                        f.write(i)
                    f.truncate()
    else:
        err = discord.Embed(title="Invalid Server ID", color=0x000000, description="")
        err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
        err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
        await ctx.send(embed=err)
        channel = bot.get_channel(1006979964299661333)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log = discord.Embed(title="ATTENTION", color=0x000000, description="")
        log.add_field(name="UNKOWN SERVER ID", value="Someone invited me to a retarded server", inline=False)
        log.add_field(name="Server:", value=f"{ctx.message.guild.id}", inline=False)
        log.add_field(name="Server Invite", value= (link), inline=False)
        await channel.send(embed=log)

@random.error
async def attack_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"𝙎𝙚𝙧𝙖𝙥𝙝 | 𝘾𝙤𝙤𝙡𝙙𝙤𝙬𝙣",description=f"Jesus wait {error.retry_after:20f} seconds ya greedy cunt.", color=0x000000)
            await ctx.send(embed=em)

@bot.command()
@commands.cooldown(1,85, commands.BucketType.user)
async def disney(ctx):
    if ctx.message.guild.id in servers:
        with open('dis.txt','r') as txt:
            content= txt.readline()
            gen = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            gen.add_field(name="Account Grabbed", value= (content) , inline=False)
            await ctx.author.send(embed=gen)
            res = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", color=0x000000)
            res.add_field(name="Account Grabbed", value= ("Please check your dms") , inline=False)
            await ctx.send(embed=res)
            print(f"    {ctx.author} has genned a disney+ account in {ctx.channel}")
            channel = bot.get_channel(1006979964299661333)
            log = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙇𝙤𝙜𝙨", color=0x000000)
            log.add_field(name=f"{ctx.author}", value=f"has genned a disney+ account in {ctx.channel}", inline=False)
            await channel.send(embed=log)
            cool = discord.Embed(title=f"{ctx.author} your 85 second cooldown has started...", color=0x000000)
            await ctx.send(embed=cool)
            with open("dis.txt", "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != (content):
                        f.write(i)
                    f.truncate()  
    else:
        err = discord.Embed(title="Invalid Server ID", color=0x000000, description="")
        err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
        err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
        await ctx.send(embed=err)
        channel = bot.get_channel(1006979964299661333)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log = discord.Embed(title="ATTENTION", color=0x000000, description="")
        log.add_field(name="UNKOWN SERVER ID", value="Someone invited me to a retarded server", inline=False)
        log.add_field(name="Server:", value=f"{ctx.message.guild.id}", inline=False)
        log.add_field(name="Server Invite", value= (link), inline=False)
        await channel.send(embed=log)

@disney.error
async def attack_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"𝙎𝙚𝙧𝙖𝙥𝙝 | 𝘾𝙤𝙤𝙡𝙙𝙤𝙬𝙣",description=f"Jesus wait {error.retry_after:20f} seconds ya greedy cunt.", color=0x000000)
            await ctx.send(embed=em)

@bot.command()
async def credits(ctx):
    if ctx.message.guild.id in servers:
        credits = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝘾𝙧𝙚𝙙𝙞𝙩𝙨",color=0x000000)
        credits.add_field(name="Maker:", value="Paradym", inline=False)
        credits.add_field(name="Info", value="This bot is just proof of concept and will remain private to dev only /nIf you want this bot for urself then dm me and we can make a deal /nIfthere are no accounts left to grab ill try to get more and fill in stock /nBare in mind some of the accounts may be locked so just grab another one /nI get these accounts from other sources so please be pacient if they dont work or are locked", inline=False)
        await ctx.send(embed=credits)
        print(f"    {ctx.author} used credits in {ctx.channel}")
        channel = bot.get_channel(1006979964299661333)
        log = discord.Embed(title="𝙎𝙚𝙧𝙖𝙥𝙝 | 𝙇𝙤𝙜𝙨", color=0x000000)
        log.add_field(name=f"{ctx.author}", value=f"used credits in {ctx.channel}", inline=False)
        await channel.send(embed=log)
    else:
        err = discord.Embed(title="Invalid Server ID", color=0x000000, description="")
        err.add_field(name="ERROR:", value="The dumbass who invited the bot to this server didnt realise i am private and i will not work in this server", inline=False)
        err.add_field(name="FIX:", value="If u would like to fix this issue please message Paradym#0116 to sort out a deal otherwise i aint working", inline=False)
        await ctx.send(embed=err)
        channel = bot.get_channel(1006979964299661333)
        server = f"{ctx.message.guild.id}"
        link = await ctx.channel.create_invite(max_age = 0)
        log = discord.Embed(title="ATTENTION", color=0x000000, description="")
        log.add_field(name="UNKOWN SERVER ID", value="Someone invited me to a retarded server", inline=False)
        log.add_field(name="Server:", value=f"{ctx.message.guild.id}", inline=False)
        log.add_field(name="Server Invite", value= (link), inline=False)
        await channel.send(embed=log)

with open ('bot.txt','r')as txt:
    content = txt.readlines()   
    bot.run(content)


