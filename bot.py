
import discord
import asyncio
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot  
import os


prefix = '!'
Bot = commands.Bot(command_prefix= '!')

#file = discord.File("text.txt", filename = "text.txt")
#await ctx.send("message" ,file = file)
#file(название файла в папке, филенаме= название файла в дискорде который будет




@Bot.event
async def on_ready():

	print("Bot is online!")
Bot.remove_command('help')	
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

@Bot.command(pass_context=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	if ctx.author.id in [603860059595866115,410404778678681610,620324517990105108,543108160748257304,712365589271674894,635484724718206976,506886660567334934]:
		await member.ban(reason=reason)
		await ctx.send('User {0} banned! '.format(member) + 'Причина : {0}'.format(reason))
	else:
		await ctx.send('Ты не пройдёёшь!')
@Bot.command(pass_context=True)
async def kick(ctx, member: discord.Member, *, reason=None):
	if ctx.author.id in [603860059595866115,410404778678681610,620324517990105108,543108160748257304,712365589271674894,635484724718206976,506886660567334934]:
		await member.kick(reason=reason)
		await ctx.send('User {0} kicked! '.format(member) + 'Причина : {0}'.format(reason))   
	else:
		await ctx.send('Ты не пройдёёшь!')		

@Bot.command(pass_context=True)
async def help(ctx):
	emb = discord.Embed(title="Информация о командах.", colour = 0x39d0d6)
	emb.add_field(name = '{}help'.format(prefix), value="Выводит информацию о командах.")
	emb.add_field(name = '{}hello'.format(prefix), value="Тестовая функция приветствия.")
	emb.add_field(name = '{}MadGunZ_Script'.format(prefix), value="Скрипт на Mad GunZ(free).")
	emb.add_field(name = '{}BlockManGoScript'.format(prefix), value="Скрипт на BlockMan GO(free).")
	emb.add_field(name = '{}WorldWarPolygonScript'.format(prefix), value="Скрипт на World War Polygon(free).")
	emb.add_field(name = '{}ChickenGunScript'.format(prefix), value="Скрипт на Chicken Gun(free).")
	emb.add_field(name = '{}ban'.format(prefix), value="С этой функцией можно забанить человека.")
	emb.add_field(name = '{}kick'.format(prefix), value="С этой функцией можно кикнуть человека.")
	await ctx.send(embed=emb)

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
