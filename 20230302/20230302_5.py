num = []
for i in range(1,6):
    num.append(int(input(f"{i}번째 숫자를 입력하세요: ")))

print(f"입력받은 숫자들: {num}")
print(max(num))
print(min(num))