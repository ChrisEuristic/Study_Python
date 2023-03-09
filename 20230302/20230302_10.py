num1 = int(input("수를 입력해주세요."))
num2 = int(input("수를 입력해주세요."))

if num1 < num2:
    num1 += num2
    num2 = num1 - num2
    num1 -= num2

while True:
    if num1 % num2 == 0:
        print(f"최대공약수는 {num2}입니다.")
        break
    else:
        temp = num1
        num1 = num2
        num2 = temp % num2