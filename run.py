import twint
import configparser
import requests
import telegram
import datetime
import time
from io import StringIO
import sys
from googletrans import Translator

configParser = configparser.RawConfigParser()   
configFilePath = r'config.txt'
configParser.read(configFilePath)

TELE_CHANNEL = configParser.get('tele', 'Channel')
TELE_BOT_TOKEN = configParser.get('tele', 'Token')
TWT_CHANNEL = configParser.get('twitter', 'Channels').strip().split(',')
INTERVAL_CHECK = int(configParser.get('twitter', 'IntervalCheck'))

bot = telegram.Bot(token=TELE_BOT_TOKEN)


def main(): 
    since = now()
    while True:
        for channel in TWT_CHANNEL:
            try: 
                print('start crawl channel ' + channel)
                data = get(channel, since)
                notify(channel, data)
            except Exception as e:
                print("ERROR " + str(e))
        since = now()
        time.sleep(INTERVAL_CHECK)

def get(channel, since):
    print('crawl channel ' + channel + ' since ' + since)
    translator = Translator()

    c = twint.Config()
    c.Username = channel
    c.Limit = 1
    c.Since = since

    save_stdout = sys.stdout
    result = StringIO()
    sys.stdout = result

    twint.run.Search(c)

    sys.stdout = save_stdout

    x = result.getvalue()
    lines = x.splitlines()
    
    l = []
    for line in lines: 
        if channel not in line:
            continue
        data = line.split(" ", 5)
        content = data[5]
        l.append({
            "raw": content,
            "tran": translator.translate(content, dest="vi").text,
        })
    return l

def now():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def notify(channel, data):
    for item in data: 
        msg = ("New message from channel @" + channel 
            + "\n============\n"
            + item["raw"] 
            + "\n============\n" 
            + item["tran"])

        sendTele(msg)

def sendTele(msg):
    print('TELE -> "' + TELE_CHANNEL + '" ===\n ' + msg)
    if not TELE_CHANNEL:
        return
    bot.sendMessage(text = msg, chat_id = TELE_CHANNEL)

if __name__ == "__main__":
    main()