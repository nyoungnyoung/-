T = int(input())
for tc in range(1, T + 1):
    origin = list(map(int, input()))
    L = len(origin)
    first = [0] * L
    cnt = 0
    while first != origin:                  # 초기값이 원래값과 같아지기 전까지 반복
        for i in range(L):                  # origin 길이만큼 돌면서
            if origin[i] != first[i]:       # origin의 i번째 인덱스와 first의 i번째 인덱스가 같지 않으면
                for j in range(i, L):       # j : i부터 L까지
                    first[j] = int(not first[j])    # first의 j번째 요소를 반전시켜주자
                cnt += 1                    # 한번 고칠때마다 cnt에 +1
    print(f'#{tc} {cnt}')