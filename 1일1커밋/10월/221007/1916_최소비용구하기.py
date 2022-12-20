import sys, heapq


# 다익스트라
def dijkstra(s):
    queue = []

    # heapq 사용하면 heappush할때마다 최소힙(기본값) 만들어짐!
    # heappop하면 가장 작은 원소 삭제됨
    heapq.heappush(queue, (s, 0))       # 시작지점 큐에 넣기(시작지점은 비용 0)
    visited[s] = 0                      # 시작지점의 비용 0으로 만들어주기

    while queue:                        # 큐가 빌때까지 반복할건데
        v, c = heapq.heappop(queue)     # 큐에서 현재위치랑 비용 꺼내오기

        # visited[v]가 c보다 작으면 더 볼 필요 없음!
        if visited[v] < c:
            continue

        # v와 연결된 도시 nv까지 가는데 드는 비용 nc
        for nv, nc in bus[v]:
            # 다음도시까지 가는데 드는 총 비용 money
            # : 현재 노드까지의 비용 c + nv까지 가는데 드는 비용 nc
            money = c + nc
            # money가 그 전에 nv까지 가는데 걸렸던 비용보다 작으면
            if money < visited[nv]:
                visited[nv] = money                     # visited[nv]에 money 저장
                heapq.heappush(queue, (nv, money))      # queue에 (nv, money) 넣어주기


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
bus = [[] for _ in range(N+1)]    # 도시 번호 : 1~N -> 그대로 인덱스로 사용
visited = [int(1e9)] * (N+1)

# 버스 노선 먼저 저장해주기!
for _ in range(M):
    S, E, cost = map(int, sys.stdin.readline().split())
    bus[S].append((E, cost))      # bus의 S번째 인덱스에 (도착지, 비용) 튜플형태로 추가

start, end = map(int, sys.stdin.readline().split())
dijkstra(start)
print(visited[end])


def daik(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        node, dist = heapq.heappop(q)
        if dist > distance[node]:
                continue
        for n in graph[node]:
            cost = dist + n[1]
            if distance[n[0]] > cost:
                heapq.heappush(q, (n[0], cost))
                distance[n[0]] = cost