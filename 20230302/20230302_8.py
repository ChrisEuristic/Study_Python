# 주사위 게임
import random


    
while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if(dice1 + dice2 == 7):
        print(f"{dice1}, {dice2} 승리")
        break
    else:
        print(f"{dice1}, {dice2} 패배")
