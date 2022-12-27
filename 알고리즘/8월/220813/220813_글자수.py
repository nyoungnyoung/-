T = int(input())
for tc in range(1, T+1):
    N = set(input())
    M = input()
    word = {}
    for i in N:
        for j in M:
            if i == j:
                if i not in word:
                    word[i] = 1
                else:
                    word[i] += 1
    print(f'#{tc} {max(word.values())}')
