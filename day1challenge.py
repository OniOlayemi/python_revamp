import re

pattern = r'\b(?:(?:(one)|(two)|(three))(?:,|\b)){3,}(?(1)|(?!))(?(2)|(?!))(?(3)|(?!))'

# Example text that contains various sentences
text = """
one, two, three
one two, one, three
one, two, one, two, three, one
"""

# Split the text into sentences based on newlines
sentences = text.strip().split("\n")
print(sentences)
# Iterate through each sentence and use the regular expression to find matches
for sentence in sentences:
    match = re.search(pattern, sentence)
    if match:
        print(f"Match found in sentence: {sentence}")
    else:
        print(f"No match found in sentence: {sentence}")

pattern = r'\b(?:(one)|(two)|(three))(?:,|\b)\b'

# Example text that contains various sentences
text = """
one, two, three
one two, one, three
one, two, one, two, three, one
"""

# Split the text into sentences based on newlines
sentences = text.strip().split("\n")

# Iterate through each sentence and use the regular expression to find matches
for sentence in sentences:
    # Find all matches of the pattern in the sentence
    matches = re.findall(pattern, sentence)
    if matches and len(matches) >= 3:
        print(f"Match found in sentence: {sentence}")
    else:
        print(f"No match found in sentence: {sentence}")

# Code with bug
'''
# Pattern with comments
pattern = (r'\d{4}   #for year'
           r'-\2{2}   # for month'
           )
# Example of text
text = '4444-33'

match = re.match(pattern, text)

if match:
    print(match)

else:
    print('no match')
'''

# Another wrong trial
'''
# Pattern with comments
pattern = (r'\d{4}   #for year'
           r'-\2{2}   # for month'
           )
# Example of text
text = '4444-33'

match = re.match(pattern, text, re.verbose)

if match:
    print(match)

else:
    print('no match')
'''

# Pattern with comments
pattern = re.compile(r'''\d{4}   # for year
                        -\d{2}   # for month
                        ''', re.VERBOSE)
# Example of text
text = '4444-33'

match = re.match(pattern, text)

if match:
    print(match)

else:
    print('no match')

# Pattern with comments
pattern = (r'\d{4}   #for year'
           r'-\2{2}   # for month'
           )
# Example of text
text = '4444-33'

match = re.match(pattern, text, re.VERBOSE)

if match:
    print(match)

else:
    print('no match')


pattern = r'http:\S'

text = 'http: //www.xyz.com'

match = re.findall(pattern, text)

print(match)

regexing = re.compile('^[abce]')

match = regexing.match('abacus')

print(match)


# The difference between python's .search and .match
#the Regex pattern
pattern = r'we are'
# Sample text
text1 = 'we are the best'
text2 = 'the best we are'
text3 = 'we are'

# Regular expression to find match
srch = re.search(pattern, text1)

if srch:
    print("text 1 search worked")
    Result = srch.group()
    print(Result)
else:
    print("text 1 did not search worked")

# Regular expression to find match
srch = re.search(pattern, text2)

if srch:
    print("text 2 search worked")
else:
    print("text 2 did not search worked")

# Regular expression to find match
srch = re.match(pattern, text3)

if srch:
    print("text 3 match worked")
else:
    print("text 3 did not match worked")

# Regular expression for a match
if srch:
    print("text 1 match worked")
else:
    print("text 1 did not match worked")

# Regular expression to find match
srch = re.match(pattern, text2)

if srch:
    print("text 2 match worked")
else:
    print("text 2 did not match worked")

# Regular expression to find match
srch = re.match(pattern, text3)

if srch:
    print("text 3 match worked")
else:
    print("text 3 did not match worked")

# One more text for the match
pattern = r'are we'
# Sample text
text1 = 'we are the best'


# Regular expression to find match
srch = re.search(pattern, text1)

if srch:
    print("new text 1 search worked")
else:
    print("new text 1 did not search worked")



pattern = r'\d+'

text = 'lucky numbers: 10, 22, 21, 34, 54, 65, 34, 65'

ty = re.findall(pattern, text)

print(ty)
list= []
for _ in re.finditer(pattern, text):
    if _.group() % 2 == 0:
        list.append(_.group())

print(list)