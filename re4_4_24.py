x = ['jjt', 'kjh']
lst = [1, 2, x, 4, 5, 6, 7, 8, 9, 0]





print(lst)

stt = str(lst)
print(stt)


print(stt)
i = " "
for j in lst:
    i = i + str(j)

stt = i
print(stt)

import re

pattern = r'[-+][0-9]*/.[0-9][0-9][cfCF]'

text = '70.99C 80F 90f -89.56c iiu 9.43f'

match = findall(pattern, text)

print(match)