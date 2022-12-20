def find(S, G):
    queue = [S]
    visited = [0] * (V + 1)
    distance = [0] * (V + 1)

    while queue:

        v = queue.pop(0)
        for i in range(1, V + 1):
            if graph[v][i] == 1 and visited[v] == 0:
                queue.append(i)
                visited[i] = 1
                distance[i] = distance[v] + 1
            if v == G:
                return distance[v]
        print(distance)
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[0] * 10 for _ in range(10)]       # V랑 E 숫자가 10보다 큰 경우 있을 수 있음
    for _ in range(E):
        i, j = map(int, input().split())
        graph[i][j] = 1
        graph[j][i] = 1
    S, G = map(int, input().split())
    print(find(S, G))