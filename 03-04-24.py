lst = [2, 3, 4, 5,6,7]
lst = lst[-1::-1]
print(lst)

import re

# Using \< and \> for word boundaries
pattern = r'\be\b'

text = 'e'

matches = re.findall(pattern, text)

print(matches)

pattern = r'\b\w*[abcdefg]\w*\b'

text = 'egg, emphasis, phrase, sees, kneel, break, brk, ham, sell, else, great, age, egg, nice, fluk, lf, geography'

matches = re.findall(pattern, text)

print(matches)

pattern = r'\b[abcdefg]\b'

text = 'abefg'

matches = re.findall(pattern, text)

print(matches)

pattern = r'[abcdefg]'

text = 'surge'

matches = re.findall(pattern, text)

print(matches)


print(matches)

pattern = r'\b[abcdefg]\b'

text = 'apple'

matches = re.findall(pattern, text)

print(matches)

print(matches)

pattern = r'\b[abcdefg]\b'

text = 'e-book'

matches = re.findall(pattern, text)

print(matches)

pattern = r'\b[abcdefg]\b'

text = 'a cat'

matches = re.findall(pattern, text)

print(matches)

pattern = r'^[abcdefg]&'

text = 'a cat'

matches = re.findall(pattern, text)

print(matches)


pattern = r'^[abcdefg]&'

text = 'a'

matches = re.findall(pattern, text)

print(matches)