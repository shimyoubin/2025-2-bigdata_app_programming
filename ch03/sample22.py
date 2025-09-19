
data = {
    'bgnde':'2025.03.01',
    'endde':'2025.02.01',
    'sj':'anjrsdlfkjs'
}

print(data)
print(type(data))
'''
    리스트는 순서가 중요함
    딕셔너리는 키가 중요해서 중복을 허용하지 않음
'''

print(data['sj'])

data['desc'] = 'sial'
print(data)

print(len(data))

print(data.keys())

for key in data.keys():
    print(key)

#key 의 순서는 랜넘 상관 없음 ㅇㅇ

print(data.values())

for value in data.values():
    print(value)

for item in data.items():
    print(item)
    print(type(item))