from ast import Delete
from turtle import title
import discord
from discord.ext import commands

#link do bota: https://discord.com/api/oauth2/authorize?client_id=979131576325652480&permissions=8&scope=bot

client = commands.Bot(command_prefix= "!")
client.remove_command("help")


@client.event
async def on_ready():
    print(" Welcome in official MOOD bot! We are glad that You are there!")
    print(" This bot was made to send newest notifications from our site!")
    print(" If you find any bug or issues with bot let us know by dming merdae#0577 on discord!")
    print(" Thanks in advance for reporting any bugs and for using this bot!")
    await client.change_presence(activity=discord.Game(name="mood.com"))
@client.command()
async def help(ctx):
    embed=discord.Embed(title="HELP", url="https://mood-ssr.vercel.app", description="What kind of help do You need? Here are some usefull commands:", color=0x4287f5)
    embed.add_field(name="!help", value="Makes appear this window", inline=False)
    embed.add_field(name="!vercel", value="Sends You link to mood.vercel", inline=False)
    embed.add_field(name="!webapp", value="Sends You link to mood.webapp", inline=True)
    embed.add_field(name="!newsletter", value="newest post from mood", inline=False)
    embed.add_field(name="!creation_date",value="Sends you creation date of mood app",inline=False)
    await ctx.channel.send(embed=embed)
@client.command()
async def vercel(ctx):
    await ctx.channel.send("https://mood-ssr.vercel.app")
@client.command()
async def creation_date(ctx):
    await ctx.channel.send("MOOD was created on Aug 8, 2021")    
@client.command()
async def webapp(ctx):
    await ctx.channel.send("https://mood-23f44.web.app/home")
@client.command()
async def newsletter(ctx):
    await ctx.author.send("weź risperidon pajacu")





