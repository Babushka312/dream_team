import re

p = re.compile(r'.+w.+')
text = '''
wonder
owner
'''
ion = p.search(text)
print(ion.group())
