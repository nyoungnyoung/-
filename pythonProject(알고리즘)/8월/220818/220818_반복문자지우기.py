T = int(input())
for tc in range(1, T + 1):
    word = input()
    stack = []
    for i in word:
        if stack:               # 스택에 요소가 있으면
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:                   # 스택이 비어있으면
            stack.append(i)

    print(f'#{tc} {len(stack)}')
