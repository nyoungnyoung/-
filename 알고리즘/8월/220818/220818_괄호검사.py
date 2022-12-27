def match(str):
    stack = []
    top = -1
    left = ['(', '{']
    right = [')', '}']
    for i in str:
        if i in left:
            top += 1
            stack.append(i)
        elif i in right:                # i가 오른쪽 괄호일때
            # stack이 비어있지 않고, 스택의 마지막 괄호가 i와 짝이 맞다면
            if top != -1 and left.index(stack[-1]) == right.index(i):
                top -= 1
                stack.pop()
            else:           # 스택이 비고 괄호가 맞으면 / 스택에 뭐가 있고 결과가 틀리면 / 스택도 비고 괄호도 틀리면
                return 0
    if top != -1:
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T + 1):
    word = input()
    result = match(word)
    print(f'#{tc} {result}')
