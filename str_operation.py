from ast import Str

mstr = 'Hello ABC'

#[start:end:skip]
msubstr = mstr[1::2]

print(mstr)

if  ('ACB') in mstr:
    print('yes value in mstr ')
else:
    print('No')


newmstr = mstr.strip()

print(newmstr)

mstr.find('d')

l = ['a'] * 5

print(l, ''.join(l))

from collections import Counter
lst = [10,11,11,10,9,90,9,8,9,3,3,2,3,2,2,22]

counter = Counter(lst)
print(counter)

s = 'are you ok?'
chk=('ok','are','you')
pun = (',','?','!')

print(s.startswith(chk))
print(s.endswith(pun))

text = 'Hello how are you'
print(text.split(' '))

s=['random1','text','foo']

# String join by mentioned seperator / Join Iterable object in case of string used / and for list with ' '
# print(dir(text))
print('/'.join(text))
print(' '.join(s))