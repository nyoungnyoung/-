
T = int(input())
for i in range(T):               # T만큼 반복해서
    R, S = input().split()  # R, S : 문자열
    R = int(R)
    for j in range(len(S)):  # S의 길이만큼 반복
        print(S[j] * R, end='')
    i += 1
    print()
