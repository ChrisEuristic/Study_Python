# 문자열에서 알파벳 빈도수 구하기
text = "Hello, world!"

알파벳 = set(text)
빈도수 = {}

for i in list(알파벳):
    합계 = 0
    for j in text:
        if i == j:
            합계 += 1
    빈도수[i] = 합계

print(빈도수)