days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June':30, 'July':31, 'August':31,'September':30, 'October':31, 'November':30, 'December':31}

'''
# 1번
month = input("월 입력 : ")
print(month , " : " , days.get(month))

# 2번
print(sorted(days.keys()))

# 3번
for i in days.keys():
    if days.get(i) == 31:
        print(i)

# 4번
daysItem = [(day, month) for (month, day) in days.items()]
daysItem.sort()
daysItem = [(day, month) for (month, day) in daysItem]
print(daysItem)

# 5번
month3 = input("월 3글자 입력 : ")
for i in days:
    if month3 == i[:3]:
        print(days.get(i))

'''