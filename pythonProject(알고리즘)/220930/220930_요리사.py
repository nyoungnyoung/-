from itertools import combinations, permutations

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [x for x in range(N)]
    # nCr : 가능한 재료의 조합 구하기(n개 중에서 n//2개 뽑아야 함)
    nCr = list(combinations(lst, N//2))
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 20000
    # nCr을 돌면서 idx의 원소에 해당하는 애들 중 2개 순열/len(nCr)-idx의 원소에 해당하는 애들 중 2개 순열
    for idx in range(len(nCr)//2):
        # food_a / food_b : 음식 만들면서 생기는 시너지들의 순열
        food_a = list(permutations(nCr[idx], 2))
        food_b = list(permutations(nCr[-1-idx], 2))
        val_a, val_b = 0, 0         # val_a / val_b : A음식, B음식의 시너지
        for k in food_a:
            i, j = k
            val_a += arr[i][j]
        for k in food_b:
            i, j = k
            val_b += arr[i][j]
        val = abs(val_a - val_b)
        if minV > val:
            minV = val
    print(f'#{tc} {minV}')
