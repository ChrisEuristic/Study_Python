# 학생성적을 딕셔너리로 저장하고 성적 평균 계산 프로그램 만들기
학생성적 = {
    "Alice": [85, 90, 95],
    "Bob": [75, 80, 85],
    "Charlie": [95, 95, 95]
}

for key in 학생성적.keys():
    avg = 0
    for 성적 in 학생성적.get(key):
        avg += int(성적)
    avg /= 3
    print(key, " : ", avg)