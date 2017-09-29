#packing은 tuple만 가능
t = 10, 20, 30, 'python'
print(t, type(t))

#unpacking
a,b,c,d = t
print(a,b,c,d)

#packing & unpacking
a,b,c,d = 10, 20, 30, 'haha'
print(a,b,c,d)

#unpacking error
#a,b,c = (10,20,30,40)

#unpacking extended
a, *b = (1,2,3,4)
print(a)
print(b)

*a, b = (1,2,3,4,5)
print(a)
print(b)

a, *b, c = (1,2,3,4,5)
print(a)
print(b)
print(c)