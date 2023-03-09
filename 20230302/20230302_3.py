time = int(input("1~12 숫자입력 => "))
ampm = input("am? pm? => ")
after = int(input("얼마 후? => "))

time = time + after
change = int(time / 12)
time %= 12

if time == 0:
    time = 12
else:
    if change % 2 == 1:
        if ampm == "am":
            ampm = "pm"
        else:
            ampm = "am"

        
print(f"결과 시각 : {ampm}{time}시")