i = 1
while True:
    L, P, V = map(int, input().split())
    # V // P * L (L일 꽉 채워서 이용 가능한 날짜)
    # V % P (남은 날짜)와 L 중에서 더 작은 걸
    # 결과 값(result)에 더해줘야 함!
    if L == P == V == 0:
        break
    result = (V // P * L) + min((V % P), L)
    print(f'Case {i}: {result}')
    i += 1