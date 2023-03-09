cm = float(input("길이를 입력하세요."))
if cm < 0:
    print("잘못 입력하였습니다.")
else:
    print(f"{cm/2.54:.2f}")