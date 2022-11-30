from ast import Str


mstr = 'Hello ABC'

#[start:end:skip]
msubstr = mstr[1::2]

print(mstr)

if  'ab' or 'ABC' in mstr:
    print('yes')
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