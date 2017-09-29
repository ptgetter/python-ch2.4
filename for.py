a = ['cat', 'cow', 'tiger']

for animal in a:
    print(animal)

for x in range(10):
    print(x, end=" ")
else:
    print()

l = [('둘리', 10), ('마이콜', 20), ('도우넛', 30)]

for data in l:
    print('이름:%s, 나이:%d' % data)

print('\n')

for name, age in l:
    print('이름:{0}, 나이:{1}'.format(name, age))

