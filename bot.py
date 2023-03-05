from move_profile import move_to_profile
from delete_profile import delete_to_profile
from moodle_client import MoodleClient2
from client_nex import Client as moodle
from moodle import delete
import shutil
import asyncio
import tgcrypto
import aiohttp
import aiohttp_socks
import yt_dlp
import os
import aiohttp
import re
import requests
import json
import psutil
import platform
import pymegatools
from pyrogram import Client , filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from json import loads,dumps
from pathlib import Path
from os.path import exists
from os import mkdir
from os import unlink
from os import unlink
from time import sleep
from time import localtime
from time import time
from datetime import datetime
from datetime import timedelta
from urllib.parse import quote
from urllib.parse import quote_plus
from urllib.parse import unquote_plus
from random import randint
from re import findall
from yarl import URL
from bs4 import BeautifulSoup
from io import BufferedReader
from aiohttp import ClientSession
from py7zr import SevenZipFile
from py7zr import FILTER_COPY
from zipfile import ZipFile
from multivolumefile import MultiVolume

#Datos
api_id = 9910861
api_hash = "86e927460a8998ba6d84e9c13acfda95"
bot_token = '6281846554:AAEQ97AM-d289ADS-bhJdAEpBvnHhF2crYY'
#Channel_Id = chanel_id
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
boss = ['UHTRED_OF_BEBBANBURG','Stvz20']#usuarios supremos
Configs = {"uclv":'',"gtm":"","uvs":"","ltu":"a816210ff41853b689c154bad264da8e", 
			"ucuser": "", "ucpass":"","uclv_p":"", "gp":'socks5://190.15.159.152:10089', "s":"On", 
			'UHTRED_OF_BEBBANBURG': {'z': 99,"m":"u","a":"c","t":"y"}, 
			'Stvz20': {'z': 99,"m":"u","a":"c","t":"y"}, 
			'Locura05': {'z': 99,"m":"u","a":"c","t":"y"}, 
			'mcfee2828': {'z': 99,"m":"u","a":"c","t":"y"}
			}

Urls = {} #urls subidos a educa
Urls_draft = {} #urls para borrar de draft
Config = {} #configuraciones privadas de moodle
id_de_ms = {} #id de mensage a borrar con la funcion de cancelar
root = {} #directorio actual
downlist = {} #lista de archivos descargados
procesos = 0 #numero de procesos activos en el bot

#inicio
@bot.on_message(filters.command("start", prefixes="/") & filters.private)
async def start(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	zipps = str(Configs[username]["z"])
	auto = Configs[username]["t"]
	total = shutil.disk_usage(os.getcwd())[0]
	used = shutil.disk_usage(os.getcwd())[1]
	free = shutil.disk_usage(os.getcwd())[2]	
	uname = platform.uname()
	svmem = psutil.virtual_memory()
	a = await client.send_message(username,'**Por Favor Espere...**')
        #msg = f"Hola☺️⚡🤖\n"
	msg = f"**ADM BoT 🤖@Stvz20🤖**\n"
	#msg += f"➣𝘡𝘪𝘱𝘴 𝘤𝘰𝘯𝘧𝘪𝘨𝘶𝘳𝘢𝘥𝘰𝘴 𝘢: **{zipps}MB**\n"	    
	#msg += "➣𝘌𝘴𝘵𝘢𝘥𝘰 𝘥𝘦𝘭 𝘣𝘰𝘵: "+ Configs["s"] +"\n"
	#if auto == "y":
	#	msg += "➣𝘈𝘶𝘵𝘰𝘮𝘢𝘵𝘪𝘤 𝘜𝘱: **On**\n\n"
	#else:
	#	msg += "➣𝘈𝘶𝘵𝘰𝘮𝘢𝘵𝘪𝘤 𝘜𝘱: **Off**\n\n"
	if Configs[username]["a"] == "l":
		mode = "☁️Subida☁️ ➥ **UVS.LTU**\n"
	elif Configs[username]["a"] == "h":
		mode = "☁️ Subida ☁️ ➥ **GTM**\n"
	elif Configs[username]["a"] == "d":
		mode = "☁️ 𝓝𝓾𝓫𝓮 𝓟𝓮𝓻𝓼𝓸𝓷𝓪𝓵 ☁️\n\n"
	elif Configs[username]["a"] == "a":
		mode = "➣𝘜𝘤𝘭𝘷 ➥ **Directs Links (Procfile)**\n"
	else:
		mode = "**☁️ Enlaces de Descaga Directa ☁️**\n"
	msg += "**Bienvenido A este Maravilloso Sistema de Descaga, De Ante mano Gracias por utilizar Nuestros Servicios❤️**\n"
	#msg += f"➣𝘚𝘺𝘴𝘵𝘦𝘮: **{uname.system}**\n"
	#msg += f"➣𝘔𝘢𝘤𝘩𝘪𝘯𝘦: **{uname.machine}**\n\n"
	#msg += "**📈Info CPU📈**\n"
	#msg += f"**Procesadores Lógicos**: **{psutil.cpu_count(logical=False)}**"
	#msg += f"\n➣𝘛𝘰𝘵𝘢𝘭 𝘤𝘰𝘳𝘦𝘴: **{psutil.cpu_count(logical=True)}**"
	#msg += f"\n**📉CPU Usado📉**: **{psutil.cpu_percent()}%**\n\n"
	#msg += "**Info Memoria RAM**\n"
	#msg += f"**⚙️Total: **{sizeof_fmt(svmem.total)}**\n"
	#msg += f"**⚙️Libre: {sizeof_fmt(svmem.available)}**\n"
	#msg += f"** Usado: {sizeof_fmt(svmem.used)}**\n"
	#msg += f"**Memoria RAM Usada: **{sizeof_fmt(svmem.percent)}%**\n\n"
	msg += f"**Usa el Comando:\n/uvs > Para usar La Nube uvs.ltu\n/gtm > Para Usar La Nube GTM**\n"
	#msg += f"➣𝘛𝘰𝘵𝘢𝘭 𝘴𝘵𝘰𝘳𝘢𝘨𝘦: **{sizeof_fmt(used)}** / **{sizeof_fmt(total)}**\n"
	#msg += f"➣𝘍𝘳𝘦𝘦 𝘴𝘵𝘰𝘳𝘢𝘨𝘦: **{sizeof_fmt(free)}**\n\n"
	msg += mode
	await a.edit(msg)




print("started")
bot.start()
#bot.send_message(5416296262,'BoT Iniciado')
bot.loop.run_forever()
