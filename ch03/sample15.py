import copy

list_ = ['a','b', ' c', 'sd', 'df', 'sdf','. e']

new_value = list_[::2]

print(list_)
print(new_value)

list_[0] = '11'

print('-'*30)
print(list_)
print(new_value)

#---------------------------------------
print('-'*30)
list_ = [['a','b'], [' c', 'sd'], ['df', 'sdf'],'e']

#new_value = list_[::] # 깊은 복사가 아님
new_value = copy.deepcopy(list_)

print(list_)
print(new_value)

list_[0][0] = '11'

print('-'*30)
print(list_)
print(new_value)

del new_value
#print(new_value) 삭제 되서 오류남