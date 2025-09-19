
data = {
    'bgnde',
    'endde',
    'sj'
}
#set임 집합값
print(data)
print(type(data))

data.add('title')
data.add('desc')

print(data)
print(type(data))

data.remove('sj')
print(data)

if 'sj' in data:

    data.remove('sj')
else:
    print('hot here')

print(data)
