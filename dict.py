#생성
d={'basketball':5, 'soccer':11, 'baseball':9}
print(d, type(d))

print(d['basketball'])

d['volleyball'] = 6
print(d)

print(len(d))
print('soccer' in d)
print('test' in d)


d= dict()
print(d)

d=dict(one=1,two=2)
print(d)

d = dict([('one', 1), ('two', 2)])   # tuple list
print(d)

keys = ('one', 'two', 'three')
values = (1, 2, 3)
d = dict(zip(keys, values))
print(d)

#사전키는 변경불가능한 타입
d={} # 또는 dict()
print(d, type(d))
d[True] = 'True'
d[10] = 'ten'
d['twenty'] = 20
d[(1,2,3)] = '6'
print(d)

#메서드
keys = d.keys()
print(keys)
print(type(keys))

for key in keys:
    print('{0}:{1}'.format(key, d[key]))

values = d.values()
print(values)
print(type(values))

items = d.items()
print(items)

for item in items:
    print(item)
    print('{0}:{1}'.format(item[0], item[1]))

print()
for key, value in items:
    print('{0}:{1}'.format(key, value))



phone = {'둘리': '010-0000-0000', '도우넛': '010-1111-1111', '또치': '010-2222-2222'}
p = phone.copy()
print(phone)
print(p)
phone['마이콜'] = '010-3333-3333'
print(phone)
print(p)

n = phone.get('둘리')
print(n)

n = phone.get('길동')
print(n)
# 에러
# n = phone['길동']

n = phone.get('길동', '000-0000-0000')
print(n)
print(phone)

n = phone.setdefault('길동', '000-0000-0000')
print(n)
print(phone)

n = phone.pop('둘리')
print(n)
print(phone)

n = phone.popitem()
print(n, type(n))
print(phone)

phone.update({'둘리': '010-1111-1111', '길동': '010-5555-5555'})
print(phone)

phone.clear()
print(phone)




d = {'c': 3, 'a': 1, 'b': 2}
for key in d:
    print(key, end=' ')
else:
    print()


for key in d:
    print(str(key) + ":" + str(d[key]), end=' ')
else:
    print()

for key in d:
    print("{0}:{1}".format(key, d[key]), end=' ')
else:
    print()

for key in d.keys():
    print("{0}:{1}".format(key, d[key]), end=' ')
else:
    print()

for key, value in d.items():
    print("{0}:{1}".format(key, value), end=' ')
else:
    print()