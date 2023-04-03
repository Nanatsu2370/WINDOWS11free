import shutil
import asyncio
import tgcrypto
import aiohttp
import aiohttp_socks
#import yt_dlp
import os
import aiohttp
import re
import requests
import json
import psutil
import platform
import pymegatools
from pyrogram import Client , filters
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
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
from moodle_client import MoodleClient2
import xdlink
from client_nex import Client as moodle
import NexCloudClient
import threading

#BoT Configuration Variables
api_id = 9548711
api_hash = "4225fbfa50c5ac44194081a0f114bdd1"
bot_token = '6055250142:AAGWXX1p_k9H9F13MJsLBGdHKoMMkWx6-xc'
Channel_Id = -1001510816478
msg_id = 3
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
boss = ['Nanatsu2370','Stvz20']#usuarios supremos
Configs = {"vcl":'035649148fac062426ee3c5d72a6ec1f',"gtm":"cc9c6b9c0523b17c7f00202993ceac1c","uvs":"4ce7bf57fb75c046a9fbdd30900ea7c9","ltu":"a816210ff41853b689c154bad264da8e",
			"ucuser": "", "ucpass":"","uclv_p":"", "gp":'socks5://181.225.255.48:9050', "s":"On", 
			'Nanatsu2370': {'z': 99,"m":"u","a":"c","t":"y"}, 
			'Stvz20': {'z': 99,"m":"u","a":"upltu","t":"y"}
			}
start = time()
Urls = {} #urls subidos a educa
Urls_draft = {} #urls para borrar de draft
Config = {} #configuraciones privadas de moodle
id_de_ms = {} #id de mensage a borrar con la funcion de cancelar
root = {} #directorio actual
downlist = {} #lista de archivos descargados
procesos = 0 #numero de procesos activos en el bot

##Base De Datos

###############

###Buttons
@bot.on_message(filters.command('timer') & filters.private)
async def timer(bot, message):
    uptime = get_readable_time(time() - start)
    username = message.from_user.username
    msg =  await bot.send_message(username, uptime)
    global seg
    if seg != localtime().tm_sec:
        try: await message.edit(msg)
        except:pass
    seg = localtime().tm_sec

nubess = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('☁️ UVS.LTU ☁️', callback_data="uvs"),
        InlineKeyboardButton('☁️ GTM ☁️', callback_data="gtm"),
        InlineKeyboardButton('☁️CMW ☁️', callback_data="cmw")],
        [InlineKeyboardButton('☁️Eduvirtual☁️', callback_data="edu"),
        InlineKeyboardButton('☁️Nube Personal☁️', callback_data="personal"),
        InlineKeyboardButton('☁️Extra☁️', callback_data="extra")],
        [InlineKeyboardButton('☁️ Eduvirtual Preconfigurada ☁️', callback_data="edup")],
        [InlineKeyboardButton('ᐊᐊᐊᐊᐊ', callback_data="home")
        ]]
    )
hom = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('☁️ Seleccionar Nube ☁️', callback_data="nubes")],
        [InlineKeyboardButton('⚙️ Info De Usuario ⚙️', callback_data="infouser"),
        InlineKeyboardButton('📈 Info Del BoT 📈', callback_data="infobot")],
        [InlineKeyboardButton('⚠️🆘⛑️ Ayuda ⛑️ 🆘 ⚠️', callback_data="ayuda")
        ]]
    )
atras = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ᐊᐊᐊᐊᐊ', callback_data="home")
        ]]
    )
delete = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🗑️Borrar Todo📂🗑️', callback_data="delet")
        ]]
    )
@bot.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    username = msg.from_user.username
    if msg.data == "nubes":
        await msg.message.edit(
            text="Seleccione La Nube☁️ a Subir:",
            reply_markup=nubess
        )
    elif msg.data == "uvs":
        Configs[username]["m"] = "u"
        Configs[username]["a"] = "upltu"
        Configs[username]["z"] = 19
        await send_config()
        await msg.message.edit(
            text="Ha Seleccionado la Nube☁️: uvs.ltu\nTamaño de Zips de la Nube☁️: 19 Mb",
            reply_markup=nubess
        )
    elif msg.data == "gtm":
        Configs[username]["m"] = "u"
        Configs[username]["a"] = "upgtm"
        Configs[username]["z"] = 7
        await send_config()
        await msg.message.edit(
            text="Ha Seleccionado la Nube☁️: GTM\nTamaño de Zips de la Nube☁️: 7 Mb",
            reply_markup=nubess
        )
    elif msg.data == "cmw":
        Configs[username]["m"] = "u"
        Configs[username]["a"] = "upcmw"
        Configs[username]["z"] = 10
        await send_config()
        await msg.message.edit(
            text="Ha Seleccionado la Nube☁️: CMW\nTamaño de Zips de la Nube☁️: 499 Mb",
            reply_markup=nubess
        )
    elif msg.data == "edu":
        Configs[username]["m"] = "eduvirtual"
        Configs[username]["a"] = "eduvirtual"
        Configs[username]["z"] = 500
        Config[username]["username"] = "---"
        Config[username]["password"] = "---"
        await send_config()
        await msg.message.edit(
            text="Ha Seleccionado la Nube☁️: Edvirtual\nTamaño de Zips de la Nube☁️: 500 Mb\n\nTenga en cuenta q está configuración es solo si posee una cuenta en la misma o de lo contrario no podrá Utilizarla, use /auth para añadir los datos",
            reply_markup=nubess
        )
    elif msg.data == "edup":
        Configs[username]["m"] = "edup"
        Configs[username]["a"] = "edup"
        Configs[username]["z"] = 500
        Config[username]["username"] = "miltongg"
        Config[username]["password"] = "1234567i"
        Config[username]["host"] = "https://eduvirtual.uho.edu.cu/"
        Config[username]["repoid"] = 3
        await send_config()
        await msg.message.edit(
            text="Ha Seleccionado la nube ☁️ Eduvirtual Preconfigurada",
            reply_markup=nubess
        )
    elif msg.data == "personal":
        Configs[username]["m"] = "personal"
        Configs[username]["a"] = "personal"
        Configs[username]["z"] = 100
        await send_config()
        await msg.message.edit(
            text="Ha Seleccionado la Nube☁️: Subida a Nube Personal\nTamaño de Zips de la Nube☁️: 100 Mb\n\nUse /auth para añadir los datos de su cuenta personal",
            reply_markup=nubess
        )
    elif msg.data == "extra":
        Configs[username]["m"] = "u"
        Configs[username]["a"] = "vcl"
        Configs[username]["z"] = 299
        await msg.message.edit(
            text="Ha Seleccionado la Nube☁️: Extra\nTamaño de Zips de la Nube☁️: 299 Mb",
            reply_markup=nubess
        )
    elif msg.data == "home":
        await msg.message.edit(
            text="Hola 👋🏻 a Stvz20_Upload, Bienvenido a este sistema de Descargas, estamos simpre para tí, y ayudarte a descagar cualquier archivo multimedia que desees☺️",
            reply_markup=hom
        )
    elif msg.data == "infouser":
        usuario = Config[username]["username"]
        passw = Config[username]["password"]
        host_moodle = Config[username]["host"]
        rid = Config[username]["repoid"]
        rar = Configs[username]["z"]
        mens = f"**Configuración ⚙️ @{username}**\n"
        mens += f"**User: {usuario}\nPasword: {passw}\nhost: {host_moodle}\nRepoID: {rid}\nZips: {rar}\n\n**"
        if Configs[username]["a"] == 'upgtm':
            subida = 'GTM ☁️'
        elif Configs[username]["a"] == 'upltu':
            subida = 'uvs.ltu ☁️'
        elif Configs[username]["a"] == 'upcmw':  
            subida = 'CMW ☁️' 
        elif Configs[username]["a"] == 'eduvirtual':
            subida = 'Eduvirtual ☁️'
        elif Configs[username]["a"] == 'vcl':
            subida = 'Nube Extra ☁️'
        else:   
            subida = 'Nube Personal ☁️'
        mens += f"**Nube En Uso: {subida}**"
        if Configs[username]["a"] == 'edup':
            await msg.message.edit(
                text='Estas usando una nube ☁️ a la que no puedes ver sus credenciales',
                reply_markup=atras
            )
        else:
            await msg.message.edit(
                text=mens,
                reply_markup=atras
            )
    elif msg.data == "delet":
        shutil.rmtree("downloads/"+username+"/")
        root[username]["actual_root"] = "downloads/"+username
        await msg.message.edit(
            text="⚠️🗑️ Archivos Borrados 🗑️⚠️",
        )

def get_readable_time(seconds: int) -> str:
    count = 0
    readable_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", " days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        readable_time += time_list.pop() + ", "
    time_list.reverse()
    readable_time += ": ".join(time_list)
    return readable_time

#Funcion
seg = 0
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
           return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0 
    return "%.2f%s%s" % (num, 'Yi', suffix)

def files_formatter(path,username):
    rut = str(path)
    filespath = Path(str(path))
    result = []
    dirc = []
    final = []
    for p in filespath.glob("*"):
        if p.is_file():
           result.append(str(Path(p).name))
        elif p.is_dir():
             dirc.append(str(Path(p).name))
    result.sort()
    dirc.sort()
    msg = f'**Ruta: **`{str(rut).split("downloads/")[-1]}`\n\n'
    if result == [] and dirc == [] :
        return msg , final
    for k in dirc:
        final.append(k)
    for l in result:
        final.append(l)
    i = 0
    for n in final:
        try:
            size = Path(str(path)+"/"+n).stat().st_size
        except: pass
        if not "." in n:
            msg+=f"**╭➣❮ /seven_{i} ❯─❮ /rmdir_{i} ❯─❮ /cd_{i} ❯\n╰➣**📂Carpeta:** `{n}`\n\n" 
            i += 1
        else:
        #    i += 1
            msg+=f"**╭➣❮ /up_{i} ❯─❮ /rm_{i} ❯─❮ /dl_{i} ❯\n╰➣ {sizeof_fmt(size)} - ** `📃 {n}`\n"
            i += 1
    #msg+= f"\n**Eliminar Todo**\n    **/deleteall**"
    return msg , final

def descomprimir(archivo,ruta):
    archivozip = archivo
    with ZipFile(file = archivozip, mode = "r", allowZip64 = True) as file:
        archivo = file.open(name = file.namelist()[0], mode = "r")
        archivo.close()
        guardar = ruta
        file.extractall(path = guardar)

async def limite_msg(text,username):
    lim_ch = 1500
    text = text.splitlines() 
    msg = ''
    msg_ult = '' 
    c = 0
    for l in text:
        if len(msg +"\n" + l) > lim_ch:		
            msg_ult = msg
            await bot.send_message(username,msg, reply_markup=delete)	
            msg = ''
        if msg == '':	
            msg+= l
        else:		
            msg+= "\n" +l	
        c += 1
        if len(text) == c and msg_ult != msg:
            await bot.send_message(username,msg, reply_markup=delete)

def update_progress_bar(inte,max):
    percentage = inte / max
    percentage *= 100
    percentage = round(percentage)
    hashes = int(percentage / 5)
    spaces = 20 - hashes
    progress_bar = "[ " + "•" * hashes + "•" * spaces + " ]"
    percentage_pos = int(hashes / 1)
    percentage_string = str(percentage) + "%"
    progress_bar = progress_bar[:percentage_pos] + percentage_string + progress_bar[percentage_pos + len(percentage_string):]
    return(progress_bar)

def iprox(proxy):
    tr = str.maketrans(
        "@./=#$%&:,;_-|0123456789abcd3fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ZYXWVUTSRQPONMLKJIHGFEDCBAzyIwvutsrqponmlkjihgf3dcba9876543210|-_;,:&%$#=/.@",
    )
    return str.translate(proxy[::2], tr)

#Acceso de Uso al BoT
def acceso(username):
    if username in Configs or username in boss:
        if exists('downloads/'+str(username)+'/'):pass
        else:os.makedirs('downloads/'+str(username)+'/')
       # else:os.makedirs(str(username)+'/')	
        try:Urls[username]
        except:Urls[username] = []
        try:Config[username]
        except:Config[username] = {"username":"","password":"","repoid":"","host":""}
        try:id_de_ms[username]
        except:id_de_ms[username] = {"msg":"","proc":""}
        try:root[username]
        except:root[username] = {"actual_root":f"downloads/{str(username)}"}
        try:downlist[username]
        except:downlist[username] = []
    else:return False
     
#Conf User
async def send_config():
    try:await bot.edit_message_text(Channel_Id,message_id=msg_id,text=dumps(Configs,indent=4))
    except:pass

#Comprobacion de Procesos
def comprobar_solo_un_proceso(username):
    if id_de_ms[username]["proc"] == "Up" :
        rup = "`Por Favor Espere, Ya posee una Tarea Activa\nUse: ` **/cancel** ` para Cancelar ❌ la Actual`"
        return rup
    else:
        return False

#Maximos Procesos
def total_de_procesos():
    global procesos
    hgy = "`⚠️BoT Ocupado, Prueba más Tarde ⚠️`"
    if procesos >= 100:
        return hgy
    else:
        return False


####### Inicio Todos los Comandos ########
@bot.on_message(filters.text & filters.private)
async def text_filter(client, message):
    global procesos
    user_id = message.from_user.id
    username = message.from_user.username
    send = message.reply
    mss = message.text
    try:await get_messages()
    except:await send_config()
    if acceso(username) == False:
        await send("**⚠️🔺No Tienes Contrato Activo en Este BoT🔺⚠️\nContacta al Administrador: @Stvz20**")
        return
    else:pass
   # if "youtu.be/" in message.text or "twitch.tv/" in message.text or "youtube.com/" in message.text or "xvideos.com" in message.text or "xnxx.com" in message.text:
    #    list = message.text.split(" ")
     #   url = list[0]
     #   try:format = str(list[1])
      #  except:format = "720"
       # msg = await send("**Por Favor Espere 🔍**")
        #await client.send_message(Channel_Id,f'**@{username} Envio un link de #youtube:**\n**Url:** {url}\n**Formato:** {str(format)}p')
        #procesos += 1
        #download = await ytdlp_downloader(url,user_id,msg,username,lambda data: download_progres(data,msg,format),format)
        #if procesos != 0:
           # procesos -= 1
        #await msg.edit("**Enlace De Youtube Descargado**")
        #msg = files_formatter(str(root[username]["actual_root"]),username)
        #await limite_msg(msg[0],username)
        #return

    elif "mediafire.com/" in message.text:
        url = message.text
        if "?dkey=" in str(url):
            url = str(url).split("?dkey=")[0]
        msg = await send("**Por Favor Espere 🔍**")
        await client.send_message(Channel_Id,f'**@{username} Envio un link de #mediafire:**\n**Url:** {url}\n')
        procesos += 1
        download = await download_mediafire(url, str(root[username]["actual_root"])+"/", msg, callback=mediafiredownload)
        if procesos != 0:
            procesos -= 1
        await msg.edit("**Enlace De MediaFire Descargado**")
        msg = files_formatter(str(root[username]["actual_root"]),username)
        await limite_msg(msg[0],username)
        return

    elif "https://mega.nz/file/" in message.text:
        url = message.text
        mega = pymegatools.Megatools()
        try:
            filename = mega.filename(url)
            g = await send(f"Descargando {filename} ...")
            data = mega.download(url,progress=None)	
            procesos += 1
            shutil.move(filename,str(root[username]["actual_root"]))
            await g.delete()
            msg = files_formatter(str(root[username]["actual_root"]),username)
            await limite_msg(msg[0],username)
            if procesos != 0:
                procesos -= 1
            return
        except Exception as ex:
            if procesos != 0:
                procesos -= 1
            if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
            else:
                await send(ex)	
                return
    elif "https://mega" in message.text:
        url = message.text
        mega = pymegatools.Megatools()
        try:
            filename = mega.filename(url)
            g = await send(f"Descargando {filename} ...")
            data = mega.download(url,progress=None)	
            procesos += 1
            shutil.move(filename,str(root[username]["actual_root"]))
            await g.delete()
            msg = files_formatter(str(root[username]["actual_root"]),username)
            await limite_msg(msg[0],username)
            if procesos != 0:
                procesos -= 1
            return
        except Exception as ex:
            if procesos != 0:
                procesos -= 1
            if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
            else:
                await send(ex)	
                return
    elif '/wget' in mss:
        j = str(root[username]["actual_root"])+"/"
        url = message.text.split(" ")[1]
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                try:
                    filename = unquote_plus(url.split("/")[-1])
                except:
                    filename = r.content_disposition.filename	
                fsize = int(r.headers.get("Content-Length"))
                msg = await send("7**Por Favor Espere 🔍**")
                procesos += 1
                await client.send_message(Channel_Id,f'**@{username} Envio un #link :**\n**Url:** {url}\n')
                f = open(f"{j}{filename}","wb")
                newchunk = 0
                start = time()
                async for chunk in r.content.iter_chunked(1024*1024):
                    newchunk+=len(chunk)
                    await mediafiredownload(newchunk,fsize,filename,start,msg)
                    f.write(chunk)
                f.close()
                file = f"{j}{filename}"
                await msg.edit("**Enlace Descargado**")
                if procesos != 0:
                    procesos -= 1
                else:pass
                msg = files_formatter(str(root[username]["actual_root"]),username)
                await limite_msg(msg[0],username)
                return

    elif "/up_" in mss:
          comp = comprobar_solo_un_proceso(username) 
          if comp != False:
              await send(comp)
              return
          else:pass
          total_proc = total_de_procesos()
          if total_proc != False:
              await send(total_proc)
              return
          else:pass
          list = int(message.text.split("_")[1])		
          msgh = files_formatter(str(root[username]["actual_root"]),username)
          try:
              path = str(root[username]["actual_root"]+"/")+msgh[1][list]
              msg = await send(f"Archivo 
