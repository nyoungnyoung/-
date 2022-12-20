import sys

n = int(sys.stdin.readline())
stack = []
result = []
cnt = 1
tmp = True
for _ in range(n):
    num = int(sys.stdin.readline())
    # cnt가 num와 같아질때까지 +1 해주면서 stack에 push
    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1
    # cnt 가 num와 같아지면 while문 탈출
    # stack 제일 마지막에 들어가있는 숫자가 num와 같으면 pop
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    # 만족하지 않는 경우 tmp를 False로 바꿔주고 break
    else:
        tmp = False
        break
# tmp 가 False면 NO 출력
if not tmp:
    print('NO')
else:
    for i in result:
        print(i)

