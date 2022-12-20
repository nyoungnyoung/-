T = int(input())
for tc in range(1, T + 1):
    a = input()
    stack = [a[0]]
    cnt = 1
    tot = 0

    for i in range(1, len(a)):
        if a[i] == '(':
            stack.append(a[i])
            cnt += 1
        elif a[i] == ')':
            if a[i - 1] == '(':
                stack.pop()
                cnt -= 1
                tot += cnt
            else:
                stack.pop()
                tot += 1
                cnt -= 1
    print(f'#{tc} {tot}')