n = int(input("양의 정수 n을 입력하세요: "))
total = 0

for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        total += i
        
print(f"1부터 {n}까지의 자연수 중 3과 5의 배수의 합 : {total}")