n = int(input("피보나치 수열의 몇번째 항을 볼까요? => "))

pivot = [1, 1]
i = 0
while i < n-2:
    pivot.append(pivot[i] + pivot[i+1])
    i += 1
    
print(pivot[n-1])