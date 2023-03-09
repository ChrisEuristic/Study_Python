# 로또번호 만들기

import random as rd

number = set()
while len(number) < 6:
    number.add(rd.randint(1, 45))
    
numberList = list(number)
print(sorted(numberList))