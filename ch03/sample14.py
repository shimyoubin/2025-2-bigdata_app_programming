
my_book = 2005, 'pyton', 100, '2class'
your_book = [2010, 'java', 200, '2class']

#new_book = your_book[:]
new_book = your_book # 얕은복사 -> 원본바뀌면 같이 바뀜

your_book[0]=2025

print(new_book)
print(your_book)
print(my_book)
print('-'*30)

