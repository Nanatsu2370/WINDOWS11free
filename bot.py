import tgcrypto
import os
from pyrogram import Client , filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from os.path import exists
from os import mkdir
from os import unlink
from os import unlink

#BoT Configuration Variables
api_id = 9910861
api_hash = "86e927460a8998ba6d84e9c13acfda95"
bot_token = "6281846554:AAEQ97AM-d289ADS-bhJdAEpBvnHhF2crYY"
Channel_Id = -1001804018431
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

#Acceso de Uso al BoT
def acceso(username):
     if username in Config or username in boss:
         if exists('downloads/'+str(username)+'/'):pass
         else:os.makedirs('downloads/'+str(username)+'/')	
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
    try:await bot.edit_message_text(Channel_Id,message_id=3,text=dumps(Configs,indent=4))
    except:pass

#inicio
@bot.on_message(filters.command("start", prefixes="/") & filters.private)
async def start(client, message):
    username = message.from_user.username
    send = message.reply
    try:await get_messages()
    except:await send_config()
    if acceso(username) == False:
        await send("**⚠️🔺No Tienes Contrato Activo en Este BoT🔺⚠️\nContacta al Administrador: @Stvz20**")
        return
    else:pass
    msg = 'Hola'
    if Configs[username]["a"] == "l":
        mode = "**Subida hacía uvs.ltu**\n"
    msg += mode
    await send(msg)

#Comfiguracion de Nubes
@bot.on_message(filters.command("uvs_ltu", prefixes="/") & filters.private)
async def uvs_ltu(client, message):
    username = message.from_user.username
    send = message.reply
    try:await get_messages()
    except:await send_config()
    if acceso(username) == False:
        await send("**⚠️🔺No Tienes Contrato Activo en Este BoT🔺⚠️\nContacta al Administrador: @Stvz20**")
        return
    else:pass
    Configs[username]["m"] = "u"
    Configs[username]["a"] = "l"
    Configs[username]["z"] = 19
    await send_config()
    await send("**Nube ☁️ uvs.ltu Configurada**")


#Descargas de Archivos 
@bot.on_message(filters.command("down", prefixes="/") & filters.private)
async def download_archive(client: Client, message: Message):
    global procesos
    username = message.from_user.username
    send = message.reply
    try:await get_messages()
    except:await send_config()
    if comprobacion_de_user(username) == False:
	await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
	return
    else:pass
    procesos = procesos_activos(username) 
    if comp != False:
		await send(procesos)
		return
    else:pass
    total_procesos = total_de_procesos()
    if total_procesos != False:
	await send(total_proc)
	return
    else:pass
    procesos += 1
    msg = await send("𝑹𝒆𝒄𝒐𝒑𝒊𝒍𝒂𝒏𝒅𝒐 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒄𝒊ó𝒏")
    count = 0
    for i in downlist[username]:
	filesize = int(str(i).split('"file_size":')[1].split(",")[0])
	try:filename = str(i).split('"file_name": ')[1].split(",")[0].replace('"',"")	
	except:filename = str(randint(11111,999999))+".mp4"
	await bot.send_message(Channel_Id,f'**@{username} Envio un #archivo:**\n**Filename:** {filename}\n**Size:** {sizeof_fmt(filesize)}')	
	start = time()		
	await msg.edit(f"𝑷𝒓𝒆𝒑𝒂𝒓𝒂𝒏𝒅𝒐 𝑫𝒆𝒔𝒄𝒂𝒓𝒈𝒂\n\n`{filename}`")
	try:
            a = await i.download(file_name=str(root[username]["actual_root"])+"/"+filename,progress=downloadmessage_progres,progress_args=(filename,start,msg))
	    if Path(str(root[username]["actual_root"])+"/"+ filename).stat().st_size == filesize:
	    await msg.edit("𝑫𝒆𝒔𝒄𝒂𝒓𝒈𝒂 𝒆𝒙𝒊𝒕𝒐𝒔𝒂")
	    count +=1
	except Exception as ex:
	if procesos > 0:
	    procesos -= 1
	else:pass
	    if "[400 MESSAGE_ID_INVALID]" in str(ex): pass		
	    else:
	    await bot.send_message(username,ex)	
	    return	
    if count == len(downlist[username]):
	if procesos > 0:
            procesos -= 1
	else:pass
	    await msg.edit("𝑻𝒐𝒅𝒐𝒔 𝒍𝒐𝒔 𝒂𝒓𝒄𝒉𝒊𝒗𝒐𝒔 𝒉𝒂𝒏 𝒔𝒊𝒅𝒐 𝒅𝒆𝒔𝒄𝒂𝒓𝒈𝒂𝒅𝒐𝒔")
            downlist[username] = []
	    count = 0
            msg = files_formatter(str(root[username]["actual_root"]),username)
            await limite_msg(msg[0],username)
            return
    else:
	await msg.edit("**Error**")
	if procesos > 0:
	    procesos -= 1
	else:pass
            msg = files_formatter(str(root[username]["actual_root"]),username)
	    await limite_msg(msg[0],username)
	    downlist[username] = []
	    return

bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.loop.run_forever()
