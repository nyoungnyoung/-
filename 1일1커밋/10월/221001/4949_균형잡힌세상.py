from collections import deque

while True:
    word = input()
    stack = deque()
    if word == '.':
        break
    flag = True             # 짝이 맞으면 True / 안맞으면 False
    for i in word:
        # i가 왼쪽 괄호면 stack에 i넣기
        if i in '([':
            stack.append(i)
        # i가 오른쪽 괄호면 stack이 비어있지 않을때,
        # 스택의 마지막 원소랑 비교해서 짝이 맞으면 pop
        # 아니면 짝이 안맞는거!
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break
    # 스택을 다 돌았는데 flag가 False이거나, 스택이 비어있지 않으면 짝 안맞음
    if not flag or stack:
        print('no')
    else:
        print('yes')
