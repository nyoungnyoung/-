# N : 정수 개수
# lst : N개의 정수가 공백으로 구분되어 주어짐
# 단조 증가 하는 수인 Ai * Aj 값 중에서 max값 출력
# Ai * Aj 중에서 단조 증가하는 수가 없다면 -1 출력


t = int(input())

def check(value):
    value = str(value)
    for i in range(len(value) - 1):
        if value[i] > value[i+1]:
            return False
    return True


for tc in range(1, t + 1):
    n = int(input())
    data = list(map(int, input().split()))

    result = 0
    for i in range(n - 1):
        for j in range(i+1, n):
            value = data[i] * data[j]
            if check(value):
                result = max(result, value)
        if result == 0:
            result = -1

    print(f'#{tc} {result}')
