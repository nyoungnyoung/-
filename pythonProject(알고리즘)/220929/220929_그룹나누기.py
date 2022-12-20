# x의 parent 노드번호 반환
def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x                # 자기 자신이 대표번호면 x 그대로 반환


# x, y가 포함된 집합 합치기! 대표 번호 똑같게 만들어주면 됨
def union(x, y):
    parent[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parent = [x for x in range(N+1)]    # 0~N번까지 해당 번호노드의 부모 저장해줄 리스트
    visited = [0] * (N + 1)
    lst = list(map(int, input().split()))
    for i in range(0, M*2, 2):
        a, b = lst[i], lst[i+1]
        union(a, b)
    result = set()
    for i in range(1, N+1):
        result.add(find_set(i))
    print(f'#{tc} {len(result)}')
