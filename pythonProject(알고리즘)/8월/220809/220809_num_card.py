T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input()))
    counts = [0] * 10
    for i in range(N):
        counts[lst[i]] += 1         # counts 배열 만드는 과정

    result = counts[0]              # 가장 많이 나온 카드의 장 수 저장하는 변수
    card_num = 0                    # 가장 많이 나온 카드 넘버 저장하는 변수
    for i in range(len(counts)):
        if result <= counts[i]:
            result = counts[i]
            card_num = i
    print(f'#{tc} {card_num} {result}')
