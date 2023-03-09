score = int(input("학점 입력"))
if score < 40:
    grade = "1학년"
else:
    if score < 80:
        grade = "2학년"
    else:
        grade = "졸업반"
        
print(f"{grade}입니다.")