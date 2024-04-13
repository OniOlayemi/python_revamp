import re

pattern = r'\d+\b'

text = '123*'

match = re.match(pattern, text)

if match:
    print(match.start())
else:
    print('no match')


pattern = r'(?>\w+)(?>\d+)'
text = '1234abcd'

match = re.match(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found")


pattern = r'(?>\w+\d+)'

text = 'abc1234'

match = re.match(pattern, text)

if match:
    print(match.start())
else:
    print('no match')


pattern = r'(?>\w+)(?>\d+)'

text = 'abc1234'

match = re.match(pattern, text)

if match:
    print(match.start())
else:
    print('no match')

pattern = r'(?>[ab]+[oa])'

text = 'bb'

match = re.match(pattern, text)

if match:
    print(match.start())
else:
    print('no match')

pattern = r'(?>[ab]+[oa])'

text = 'ab'

match = re.match(pattern, text)

if match:
    print(match.start())
else:
    print('no match')

pattern = r'(?>[abo]+[ab])'

text = 'abooaabbbbn'

match = re.match(pattern, text)

if match:
    print(match.start())
else:
    print('no match')

pattern = r'(?>[abo]+[oa])'

text = 'abo'

match = re.match(pattern, text)

if match:
    print(match.start())
else:
    print('no match')


pattern = r'(?>[abocv]+[cv])'

text = 'abooaabbbbcvvnnn'

match = re.match(pattern, text)

if match:
    print(match.start())
else:
    print('no match')

#I am thinking nobody will give a regex syntax that have same syntax and all. so...
'''
pattern = r'\Q*^!@#$&*(){}[]|\":;.><?/\E'

text = "|}!@#$%^&*()><:?/,."


match = re.findall(pattern, text)

print(match)
'''

pattern = r'(?>[abocv]+[cv])'

text = 'abooaabcvvbbb'

match = re.match(pattern, text)

if match:
    print(match.start())
else:
    print('no match')


