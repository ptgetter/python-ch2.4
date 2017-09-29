t = ()
print(t,type(t))
t = 1, 2, 'python'
print(t, type(t))

# 원소 한개면 꼭, 를 해줘야 튜플
t2 = (1,)
nt = (1)
print(t2, type(t2))
print(nt, type(nt))

t3 = (1,2,3)

#indexing
print(t3[-2], t3[-1], t3[0], t3[1], t3[2])

#slicing
t4 = t3[1:3]
print(t4)
t5 = t3[:]
t6 = t3
print(t5)
print(t6) # 결과는 같지만 t5는 새로 만든 튜플 t6은 t3 참조

#반복
t7 = t3 * 2
print(t7)

#연결
t8 = t + (3,4,5)
print(t8)

#길이
print(len(t8))

# in, not int
print('python' in t8)
print('python' not in t8)

# immutable
#t = ('app', 'pine', 10, 20)
#t[2] = t[2] + 10


t = (1, 2, 3)

s = set(t)
print(s, type(s))

l = list(s)
print(l, type(l))

t = tuple(l)
print(t, type(t))

#swap
x = 10
y = 20
x,y = y,x
print(x,y)

#메서드가 적다
print(t.index(1))
print(t.index(3))
print(t.index(3))

#순환문
for i in t:
    print(i, end=' ')
