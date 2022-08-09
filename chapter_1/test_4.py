import re

p = r"^0"
new_word = "+996"
text = input('введи номер: ')
res = re.sub(p, new_word, text)
print(res)