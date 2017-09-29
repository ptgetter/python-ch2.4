
s1 = {1, 2, 3}
print(s1, type(s1))


l= [1,2,3,2,2,4,5,5,6]
s = set(l)
print(s)
l2 = list(s)
for n in l2:
    print(n, end=' ')
else:
    print()

s.add(10)
print(s)
s.add(1)
print(s)
s.discard(1)
print(s)

s.discard(20)
print(s)

#존재하지 않는 아이템 예외 발생
#s.remove(20)
#print(s)
s.update({1,2,6,5, 50})
print(s)
s.clear()
print(s)


s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}

s3 = s1.union(s2)
print(s3)

s4 = s1.intersection(s2)
print(s4)

s4 = s1.difference(s2)
print(s4)

#s4 = s2.difference(s1)
#print(s4)

s5 = s1.symmetric_difference(s2)
print(s5)

print(s1.issuperset(s4))
print(s5.issuperset(s1))
print(s2.issubset(s3))