import os
from pyrogram import Client, filters
from os import system as cmd
import shutil
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6280972722:AAG3GrropPJhZvfjljtgppKeeXpfpBVZG4Y"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, "أنا بوت الرفع لأرشيف . أرسل معرفاً\n\n  لبقية البوتات هنا \n\n https://t.me/sunnay6626/2 ",disable_web_page_preview=True)
@bot.on_message(filters.private & filters.incoming & filters.text)
def arhive_id11(client, message):
    global archiveid
    archiveid = message.text
    sent_message = message.reply_text('الآن أرسل الملفات ',quote=True)

@bot.on_message(filters.private & filters.incoming & filters.video | filters.audio | filters.voice | filters.document )
def _telegram_file(client, message):
 
  user_id = message.from_user.id 
  file = message
  file_path = message.download(file_name="./downloads/")
  vidname = os.path.basename(file_path)
  cmd(f'''rclone copy "{file_path}" "myarchive":"{archiveid}" ''')
  sent_message = message.reply_text('تم الرفع ',quote=True)
  cmd(f'''unlink "{file_path}" ''')


bot.run()
