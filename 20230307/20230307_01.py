def isAlphabet(str):
    for i in str:
        intI = ord(i)
        if(not(intI >= 65 and intI <= 90 or intI >= 97 and intI <= 122)):
            return False;
    return True;

str = input("문자열 입력")



print(isAlphabet(str))