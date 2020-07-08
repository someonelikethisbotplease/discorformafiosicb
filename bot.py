
import discord
import asyncio
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot  
from discord.utils import get
import youtube_dl
import os


prefix = '!'
Bot = commands.Bot(command_prefix= '!')




@Bot.event
async def on_ready():

	print("Bot is online!")
Bot.remove_command('help')	



@Bot.command()
async def join(ctx):
	channel = ctx.author.voice.channel
	voice = get(Bot.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.move_to(channel)
		await ctx.send(f'Бот присоединился к {channel}')
	else:
		voice = await discord.VoiceChannel.connect(channel)
		await ctx.send(f'Бот присоединился к {channel}')

@Bot.command()
async def leave(ctx):
	channel = ctx.author.voice.channel
	voice = get(Bot.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.disconnect()
		await ctx.send(f'Бот отключился от  {channel}')
	else:
		voice = await voice.disconnect(channel)
		await ctx.send(f'Бот отключился от  {channel}')		


@Bot.command()
async def play(ctx, url : str):
	song_there = os.path.isfile("song.mp3")

	try:
		if song_there:
			try:
				os.remove("song.mp3")
				os.remove("song.mp3")
				os.remove("song.mp3")
				os.remove("song.mp3")
			except FileNotFoundError:
				ctx.send('starting downloading it....')
			print("[log] Старый файл удалён.")
	except PermissionError: 
		print("[log] Старый файл НЕ удалён.")
	await ctx.send("Пожалуйста ожидайте")

	voice = get(Bot.voice_clients, guild = ctx.guild)

	ydl_opts = {
		'format' : 'bestaudio/best',
		'postprocessors' : [{
			'key' : 'FFmpegExtractAudio',
			'preferredcodec' : 'mp3',
			'preferredquality' : '192'
		}]
	}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl :
		print('[log] загружаю музыку...')
		ydl.download([url])


	for file in os.listdir('./'):
		if file.endswith('.mp3'):
			name = file
			print('[log] переименовываю файл {file}')
			os.rename(file, 'song.mp3')	
#
	asd = discord.FFmpegPCMAudio('song.mp3')
	asdfg = discord.VoiceClient
	voice.play(source=asd, after=None)
	voice.source = discord.PCMVolumeTransformer(voice.source)
	voice.source.volume = 0.07

	song_name = name.rsplit('-', 2)
	await ctx.send("Сейчас проигрывается музыка")











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
	emb.add_field(name = '{}join'.format(prefix), value="Подсоединяется в голосовой чат где вы.")
	emb.add_field(name = '{}leave'.format(prefix), value="Покидает голосовой чат.")
	emb.add_field(name = '{}play url'.format(prefix), value="Проигрывает то что вы указали в ссылке(ссылка должна быть на ютуб). ")
	await ctx.send(embed=emb)

@Bot.event
async def on_member_join(member):
	role = utils.get(member.guild.roles, name="Пролетар-Югенд") 


	
	

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
