from random import randint

money = 50

while money > 0:
    coin = randint(1,2)
    userChoice = int(input("앞면1, 뒷면2 입력 => "))
    if coin == userChoice:
        money += 9
        print(f"맞춤. $9 추가. 잔액 {money}")
    else:
        money -= 10
        print(f"틀림. $10 차감. 잔액 {money}")