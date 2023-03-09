d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},{'name':'Princess', 'phone':'555-3141', 'email':''},{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

# 1번
for i in d:
    if i.get('phone')[-1] == '8':
        print("end of phone number is 8 :", i.get('name'))
        
# 2번
for i in d:
    if i.get('email') == '':
        print("No have email :", i.get('name'))

# 3번
for i in d:
    if i.get('name') != '':
        print(i.get('phone'), i.get('email'))
    else:
        print('No name')