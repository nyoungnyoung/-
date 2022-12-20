import sys
T = int(sys.stdin.readline())
for tc in range(T):
    str = sys.stdin.readline()
    cnt = 0
    score = 0
    for s in range(len(str)):
        if str[s] == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)