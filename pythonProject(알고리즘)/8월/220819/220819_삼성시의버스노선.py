# 5,000개의 버스정류장
# 버스노선 N개
# i번째 버스노선 : Ai <= 정류장번호 <= Bi 인 정류장을 다님
# P개의 버스 정류장에 대해 각 정류장에 몇개의 버스 노선이 다니는지

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus = [0] * 5001                    # 버스정류장 리스트
    for i in range(1, N + 1):
        A, B = map(int, input().split())
        for _ in range(A, B + 1):       # _ : A부터 B까지
            bus[_] += 1                 # bus의 _ 인덱스에 1씩 더해주기
    P = int(input())
    result = []
    for j in range(1, P + 1):
        C = int(input())
        result += [bus[C]]              # result에 bus의 C번째 인덱스 더해주기
    print(f'#{tc}', end=' ')
    print(*result)
