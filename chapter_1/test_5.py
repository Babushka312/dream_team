# Ловим путь в URL с помощью регулярных выражений.
# Из URL localhost:8888/ilovepython извлекаем ilovepython
import re

pattern = r".+/"
new_text = ""
text = """
localhost:8888/tlovepythondfgnhmj,kjmngbvd
"""
res = re.sub(pattern, new_text, text)
print(res)