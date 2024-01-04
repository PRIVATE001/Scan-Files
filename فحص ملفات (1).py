"""
المطور @DF_GD_D
قناة @T62RS 
ممنوع تغير المصدر
"""
import requests
import os
from telebot import TeleBot
from telebot import types 
import sys

private = "Token"
API_KEY = "7f8cf5bb50c4257c102f8390093c20c3b746dc8eb603c188687bc4a5c2c622bd"
bot = telebot.TeleBot(private) 

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,f"• 📨 〈 مرحبا بك عزيزي في بوت فحص الملفات يمكنك من خلال هذا الروبورت فحص الملفات من الفايروسات يجب عليك ارسال الملف الان للفحص 〉 ^_^ ")

def check_virus(file_path):
    url = "https://www.virustotal.com/vtapi/v2/file/scan"#موقع الفص
    params = {"apikey": API_KEY}
    files = {"file": (file_path, open(file_path, "rb"))}
    response = requests.post(url, files=files, params=params)
    return response.json()

@bot.message_handler(content_types=["document"])
def handle_document(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        temp_file = "chkfile.py"
        with open(temp_file, "wb") as f:
            f.write(downloaded_file)

        virus_scan_result = check_virus(temp_file)
        os.remove(temp_file)

        if virus_scan_result["response_code"] == 1:
            bot.reply_to(message,f"• 〈 لم يتم اكتشاف اي فايروسات مريبة يمكنك استخدام الملف بامان وسلام 〉 ^_^")
        else:
            bot.reply_to(message,f"• 〈 تحذير : الملف يحتوي على فايروسات محتملة يرجى اخذ الحذر وعدم استخدام الملف 〉 🆘 ")
    except Exception as e:
        bot.reply_to(message, str(e))

print("running") 
bot.polling(none_stop=True)
"""
المطور @DF_GD_D
قناة @T62RS 
ممنوع تغير المصدر
"""