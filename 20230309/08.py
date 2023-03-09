# 1번: 1 ~ N까지의 합을 계산
def summary(n):
    total = 0
    for i in range(1, n+1):
        total += i
    print("합계 :", total)

N = int(input("n : "))
summary(N)

# 2번: 반지름을 받아 원의 둘레와 면적을 반환
def cir_area(r):
    return r ** 2 * 3.14

def cir_cirm(r):
    return r * 2 * 3.14

print(f"반지름이 3.5cm인 원의 면적은 {round(cir_area(3.5),1)}cm2 둘레는 {round(cir_cirm(3.5),1)}cm")


# 3번: den(n) 함수를 만들어 약수 리스트를 구함.
def den(n):
    약수리스트 = []
    for i in range(1, n + 1):
        if n % i == 0:
            약수리스트.append(i)
    return 약수리스트

print(den(12))