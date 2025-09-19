import copy

tuple_1 = ('a','b', ' c', 'sd', 'df')
list_2 = ['a','b', ' c', 'sd', 'df', 'sdf','. e']
# 리스트 -> 튜플 튜플 -> 리스트

tuple_to_list = list(tuple_1)
list_to_tuple = tuple(list_2)

print(type(tuple_to_list))
print(type(list_to_tuple))
