'''
# 1번
n = int(input("n : "))
m = int(input("m : "))

def draw(n, m):
    for i in range(n):
        for j in range(m):
            print("*", end='')
        print()
            
draw(n, m)
'''
'''
# 2번
def summary(n):
    total = 0

    for i in n:
        total += int(i)
        
    return total

print(summary(input("n : ")))
'''
'''
# 3
def equalsString(str1, str2):
    if str1 == str2:
        return -1
    else:
        a = max((len(str1), len(str2)))
        for i in range(a):
            if str1[i] != str2[i]:
                return i

string1 = input("문자열1: ")
string2 = input("문자열2: ")
print(equalsString(string1, string2))
'''

'''
# 4번: 문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성

def findChar(string, char):
    result = []
    position = 0
    
    for i in string:
        if char == i:
            result.append(position)
        position += 1
    
    return result

string = input("문자열: ")
char = input("문자: ")
char = char[0]
print(findChar(string, char))
'''


'''5번: 재귀함수로 1부터 n까지의 합 구하기'''

# def summary(n):
#     if n == 1:
#         return 1
#     else:
#         return n + summary(n - 1)
    
# print(summary(int(input("n? "))))
