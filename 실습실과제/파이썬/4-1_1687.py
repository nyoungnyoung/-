
password = 'abc12345!'
for i in range(3):      
    P = input()
    if P == password:
        print('로그인 성공')
        break
else:
    print('로그인 실패')

# break에 안걸리고 넘어오면 else 실행