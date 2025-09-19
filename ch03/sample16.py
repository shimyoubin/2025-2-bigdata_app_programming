import copy

list_1 = ['a','b', ' c', 'sd', 'df', 'sdf','. e']
list_2 = ['a','b', ' c', 'sd', 'df', 'sdf','. e']

list_3 = list_1 + list_2

print(list_3)

print(id(list_1))
print(id(list_2))
print(id(list_3))
'''
list_1 = list_1 + list_2
print(list_1)
'''
# append는 리스트에 리스트로 들어감 extend는 함쳐짐
list_1.extend(list_2)
print(list_1)