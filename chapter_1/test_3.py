import re

p = re.compile(r'42')
text1 = "23 street"
text2 = "42 meaning of life"
efr = p.findall(text1)
trg = p.findall(text2)
if '42' in efr:
    print('42 not in the text1')
    print('42 in the text2')
elif '42' in trg:
    print('42 not in the text1')
    print('42 in the text2')