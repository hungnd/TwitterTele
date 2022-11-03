import twint
from io import StringIO
import sys
from googletrans import Translator
translator = Translator()

c = twint.Config()

c.Username = "elonmusk"
c.Limit = 1
#c.Output = "none"
#c.Lang = "en"
c.Translate = True
c.TranslateDest = "vi"

save_stdout = sys.stdout
result = StringIO()
sys.stdout = result

twint.run.Search(c)

sys.stdout = save_stdout

x = result.getvalue()
# print(x)
# x = "1588041733639917569 2022-11-03 12:33:48 +0700 <Meta> @kunmi_16 We can hardly wait!"
print("===" + translator.translate(x, dest="vi").text)
