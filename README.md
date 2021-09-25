# Transcriber Bot
A Telegram bot to transcribe audio, video and image into text.

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/samadii/Transcribe-Bot)


## Local Deploying

1. Clone the repo
   ```
   git clone https://github.com/samadii/Transcribe-Bot
   ```
2. Now head to [this page](https://github.com/UB-Mannheim/tesseract/wiki) and install Tesseract installer. 
   
3. Use it to install Tesseract, Then Go to [this line](https://github.com/samadii/Transcribe-Bot/blob/main/bot.py#L11) and fill the inverted commas with the PATH where Tesseract is installed.

4. Replace [this PATH](https://github.com/samadii/Transcribe-Bot/blob/main/bot.py#L56) with your machine compatible one of the bellow paths :
   ```
   /usr/local/share/tessdata/
   ```
   ```
   /usr/share/tesseract-ocr/tessdata/
   ```
   ```
   /usr/share/tessdata/
   ```
   As it depends on your local machine, try with them one by one to find the compatible one.
   
5. Install all requirements using pip.
   ```
   pip3 install -r requirements.txt
   ```
6. Run the file
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
