from pyrogram import Client, filters
from funciones.func import *



API_ID = API ID
API_HASH = "API HASH"

TOKEN = "TOKEN BOT"




app = Client("bot_bin", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)



@app.on_message(filters.command("bin", prefixes="/"))
def bin_info_cmd(client, message):
    bins = message.text.split()[1:]
    mensajes = []
    
    for BIN in bins:
        BIN = BIN[:6]
        bin_info = req_api(BIN)
        
        if bin_info:
            
            BANK, BIN, BRAND, COUNTRY, CODE_MJ, LEVEL, TYPE, WEB, PHONE = bin_info
            username = message.from_user.username
            
            mensaje = f"""
<b>({icon})</b> <b><u>BinLookup</u> - [#B{BIN}]</b>
━━━━━━━━━━━━
{inf} <b>Brand:</b> <code>{BRAND}</code>
{inf} <b>Type:</b> <code>{TYPE}</code>
{inf} <b>Level:</b> <code>{LEVEL}</code>
{inf} <b>Bank:</b> <code>{BANK}</code>
{inf} <b>Country: <code>{COUNTRY}</code> [{CODE_MJ}]</b>
    
{inf} <b>Bank Web:</b> <code>{WEB}</code>
{inf} <b>Bank Phone:</b> <code>{PHONE}</code>
━━━━━━━━━━━━
"""
            
            mensajes.append(mensaje)
        else:
            
            mensaje = f"""
<b>({icon})</b> <b><u>BinLookup</u></b> <b>- [#B{BIN}]</b>
━━━━━━━━━━━━
{inf} <b>Parece que hay problemas con la API a la que estás realizando las consultas o el BIN que proporcionaste no contiene información en la API</b>
━━━━━━━━━━━━
"""
            
            mensajes.append(mensaje)
    mensaje_2 = "".join(mensajes)
    
    client.send_message(message.chat.id, mensaje_2, reply_markup=botones)
    
               

print("hola")
app.run()