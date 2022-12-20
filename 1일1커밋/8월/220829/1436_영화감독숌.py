N = int(input())
name = 666
cnt = 0
while True:
    if '666' in str(name):      # name을 문자열로 바꾸었을때 그 값에 666이라는 문자열이 포함되어있으면
        cnt += 1                # cnt 에 +1
        if cnt == N:            # cnt와 N이 같아지면 반복문 종료
            print(name)
            break
    name += 1                   # name을 1씩 증가시키는데