# Transcriber Bot
A Telegram bot to transcribe audio, video and image into text.

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/samadii/Transcribe-Bot)


## Local Deploying
Install the [FFmpeg](www.ffmpeg.org).
Make sure you have FFmpeg on the same folder as the script file if you are on Linux or Mac.

1. Clone the repo
   ```
   git clone https://github.com/samadii/Transcribe-Bot
   ```
2. Now head to [this page](https://github.com/UB-Mannheim/tesseract/wiki) and install Tesseract installer. 
   
3. Use it to install Tesseract, Then Go to [this line](https://github.com/samadii/Transcribe-Bot/blob/main/bot.py#L11) and fill the inverted commas with the PATH where Tesseract is installed.

4. Fill [this PATH](https://github.com/samadii/Transcribe-Bot/blob/main/bot.py#L56) with the path of the tessdata folder.

6. Install all requirements using pip.
   ```
   pip3 install -r requirements.txt
   ```
7. Run the file.
   ```
   python3 bot.py
   ```

## Environment Variables

#### Mandatory Vars

- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)


### Devs: 
- [@samadii](https://github.com/samadii)
