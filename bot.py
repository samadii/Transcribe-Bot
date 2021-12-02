import os
import speech_recognition as sr
import pytesseract
import requests
from PIL import Image
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import MessageEmpty
from pyromod import listen

#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

r = sr.Recognizer()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

Bot = Client(
    "TranscribeBot",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

START_TXT = """
Hi {}
I am Transcribe Bot.

> `Send me a video/audio/photo,
I will transcribe it into text.`
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/samadii/Transcribe-Bot'),
        ]]
    )


@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@Bot.on_message(filters.private & filters.photo & ~filters.edited, group=-1)
async def ocr(bot, msg):
    lang_code = await bot.ask(msg.chat.id,'`Now send the ISO language code.`\n\n[List of ISO 639-2 language codes](https://en.m.wikipedia.org/wiki/List_of_ISO_639-2_codes)', filters=filters.text, parse_mode='Markdown', disable_web_page_preview=True)
    data_url = f"https://github.com/tesseract-ocr/tessdata/raw/main/{lang_code.text}.traineddata"
    dirs = r"/app/vendor/tessdata"
    path = os.path.join(dirs, f"{lang_code.text}.traineddata")
    if not os.path.exists(path):
        data = requests.get(data_url, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'})
        if data.status_code == 200:
            open(path, 'wb').write(data.content)
        else:
            return await msg.reply("`Either the lang code is wrong or the lang is not supported.`", parse_mode='md')
    message = await msg.reply("`Downloading and Extracting...`", parse_mode='md')
    image = await msg.download(file_name=f"text_{msg.from_user.id}.jpg")
    img = Image.open(image)
    text = pytesseract.image_to_string(img, lang=f"{lang_code.text}")
    try:
        await msg.reply(text[:-1], quote=True, disable_web_page_preview=True)
    except MessageEmpty:
        return await msg.reply("`Either the image has no text or the text is not recognizable.`", quote=True, parse_mode='md')
    await message.delete()
    os.remove(image)

   
@Bot.on_message(filters.private & (filters.video | filters.document | filters.audio ) & ~filters.edited, group=-1)
async def speech2txt(bot, m):
    if m.document and not m.document.mime_type.startswith("video/"):
        return
    media = m.audio or m.video or m.document
    file_dl_path = await bot.download_media(message=m, file_name="temp/")
    lang = await bot.ask(m.chat.id,'`Now send the BCP-47 language code.`\n\n[.](https://telegra.ph/List-of-BCP-47-language-codes-09-25-2)', filters=filters.text, parse_mode='Markdown')
    msg = await m.reply("`Processing...`", parse_mode='md')
    if m.audio or file_dl_path.lower().endswith('.mp3'):
        os.system(f"ffmpeg -i {file_dl_path} temp/file.wav")
    else:
        os.system(f"ffmpeg -i {file_dl_path} -vn temp/file.wav")
    with sr.AudioFile("temp/file.wav") as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data,language=f'{lang.text}')
        except sr.UnknownValueError:
            text = "Text not recognizable"

    await m.reply(text)
    await msg.delete()
    os.remove(file_dl_path)
    os.remove("temp/file.wav")

    
Bot.run()
