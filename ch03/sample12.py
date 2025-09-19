
my_book = 2005, 'pyton', 100
your_book = [2010, 'java', 200]

 #튜플과 리스트 차이
 #데이터변경이슈

print('-'*30)
your_book[0] = 2025
your_book.append('h') # 데이터 뒤에 추가
your_book.insert(1,'name') # 위치 설정후 추가
your_book.remove('java')
print(your_book)

