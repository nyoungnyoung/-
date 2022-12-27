# 최소힙(항상 부모 노드 값 < 자식 노드 값)
def heap(n):
    global heap_cnt
    heap_cnt += 1
    tree[heap_cnt] = n
    c = heap_cnt       # 현재노드 번호
    p = c // 2         # 부모노드 번호

    # c가 1보다 크고(c == 1이면 루트노드라는거)
    # 자식노드가 부모노드보다 더 작으면 서로의 값을 바꿔줘야함
    while c > 1 and tree[c] < tree[p]:
        tree[c], tree[p] = tree[p], tree[c]
        # 그리고 c와 p의 값도 변경
        c = p
        p = c // 2
        

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    tree = [0] * (N + 1)
    heap_cnt = 0                # 힙의 가장 마지막 노드번호
    # lst의 원소들 heap에 넣기
    for i in range(N):
        heap(lst[i])
        
    # 마지막노드(heap_cnt)의 조상노드 값들의 합 result에 더해주기
    result = 0
    while heap_cnt > 1:
        heap_cnt = heap_cnt//2
        result += tree[heap_cnt]

    print(f'#{tc} {result}')