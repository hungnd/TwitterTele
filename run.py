import twint
from io import StringIO
import sys
from googletrans import Translator
translator = Translator()

c = twint.Config()

c.Username = "Meta"
c.Limit = 1
c.Since = "2022-10-01 04:37:13"

save_stdout = sys.stdout
result = StringIO()
sys.stdout = result

twint.run.Search(c)

sys.stdout = save_stdout

x = result.getvalue()
lines = x.splitlines()
# print(lines)
for line in lines: 
    data = line.split(" ", 5)
    content = data[5]
    print(translator.translate(content, dest="vi").text)

# x = "1588041733639917569 2022-11-03 12:33:48 +0700 <Meta> @kunmi_16 We can hardly wait!"
# print("===" + translator.translate(x, dest="vi").text)
