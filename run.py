import twint
import datetime
from io import StringIO
import sys
from googletrans import Translator

channel = "Meta"
since = now()
while True:
    data = get(channel, since)
    since = now()
    sleep(10)

def get(channel, since):
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
        data = line.split(" ", 5)
        content = data[5]
        l.append(translator.translate(content, dest="vi").text)

    return l

def now():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')