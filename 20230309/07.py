# 두개의 리스트에 공통으로 포함된 요소를 모두 담은 리스트 반환

import random as rd

리스트A = []
리스트B = []

for i in range(10):
    리스트A.append((rd.randint(0, 9)))
    리스트B.append((rd.randint(0, 9)))


리스트A = set(리스트A)
리스트B = set(리스트B)

print(list(리스트A))
print(list(리스트B))
print(list(리스트A & 리스트B))