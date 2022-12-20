from collections import deque
import sys
T = int(sys.stdin.readline())
for tc in range(T):
    pair = sys.stdin.readline()
    stack = deque()
    tmp = True
    for i in pair:
        if i == '(':
            # 왼쪽 괄호면 스택에 넣기
            stack.append(i)
        elif i == ')':
            # 오른쪽 괄호일때 스택이 비어있지 않으면 pop
            if stack:
                stack.pop()
            # 스택이 비어있으면 오른쪽 괄호가 더 많은거
            else:
                print('NO')
                break
    else:
        # for문 다 돌았는데 스택에 남아있는게 있으면 왼쪽괄호가 더 많은거
        if stack:
            print('NO')
        else:
            print('YES')