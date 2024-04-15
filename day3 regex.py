import re

text = '.ee.ff.gg.hh.ii.jj.kk.'

new_text = text.strip('.')

print(new_text)

newer_text = text.replace(".", "")

print(newer_text)

text2 = " the cat of the catwoman ratcat and sat"

pattern = r'\b\w+\b(?!\W+cat\b)'

match = re.findall(pattern, text2)

print(match)

text2 = " the cat of the catwoman ratcat and sat"

pattern = r'\b(?!cat)\w+\b(?!\W+cat\b)'

match = re.findall(pattern, text2)

print(match)

text2 = " the cat of the catwoman ratcat and sat"

pattern = r'\b\w+\b(?=\W+cat\b)'

match = re.findall(pattern, text2)
print(match)

text2 = " the cat of the catwoman  ratcat and sat"

pattern = r'(?<!\bcat)(?:\W+|^)(\w+)'

match = re.findall(pattern, text2)
print(match)

text = 'the a4 paper is ready for print'

pattern = r'\d'

match = re.search(pattern, text)

print(match)