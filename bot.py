
import discord
import asyncio
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot  
import os



Bot = commands.Bot(command_prefix= '!')

#file = discord.File("text.txt", filename = "text.txt")
#await ctx.send("message" ,file = file)
#file(название файла в папке, филенаме= название файла в дискорде который будет




@Bot.event
async def on_ready():

	print("Bot is online!")
	
@Bot.command(pass_context=True)
async def hello(ctx):
	if ctx.author.id == 603860059595866115:
		await ctx.send("Ты меня породил, ты меня и убьёшь")
	elif ctx.author.id == 506886660567334934:
		await ctx.send("привет мафифози")
	else:
		await ctx.send("Hello {}".format(ctx.message.author.mention))
@Bot.command(pass_context=True)
async def MadGunZ_Script(ctx):
	await ctx.send("https://shre.su/MAHC")
@Bot.command(pass_context=True)
async def BlockManGoScript(ctx):
	await ctx.send("https://shre.su/ON3K")
@Bot.command(pass_context=True)
async def WorldWarPolygonScript(ctx):
	await ctx.send("https://shre.su/C1YU")
@Bot.command(pass_context=True)
async def ChickenGunScript(ctx):
	await ctx.send("https://shre.su/55P1")



@Bot.event
async def on_member_join(member):
	role = utils.get(member.guild.roles, name="Пролетар-Югенд") 


	#newUserMessage = "Привет, {0}! Ты попал на сервер MAFIOSI CB-Youtube. Мы рады тебя тут видеть и всегда готовы тебе помочь. Чувствуй себя тут, как дома.".format(member.name)
	

	print("Короче вроде этот челик по ником " + member.name + " присоединился")
	
	#try: 
	#await Bot.send_message(member.use, newUserMessage)
	#print("Sent message to " + member.name)
	#except:
	#print("Couldn't message " + member.name)

	# give member the steam role here
	await member.add_roles(role)
	## to do this the bot must have 'Manage Roles' permission on server, and role to add must be lower than bot's top role
	print("Added role '" + role.name + "' to " + member.name)































token = os.environ.get('BOT_TOKEN')
Bot.run(token)
