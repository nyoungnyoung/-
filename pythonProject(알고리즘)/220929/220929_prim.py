'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# 1. 최소비용 노드 선택
# 2. 각 노드로 가는 최소 비용 업데이트
# 1, 2번 반복
# 강의자료에 있는 코드랑은 조금 다르게 짜봄!

V, E = map(int, input().split())
# 인접행렬 먼저 만들어주기
adj = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    s, e, weight = map(int, input().split())
    adj[s][e] = weight
    adj[e][s] = weight

# prim 시작
# 각 노드로 갈 수 있는 비용을 저장하는 배열
MST = set()
MST_value = 0
cost = [0xfffffff] * (V+1)
# 시작 정점은 0번으로! 0번에서 0번으로 가는 비용은 0
cost[0] = 0

# 모든 노드들이 선택될 때 까지 반복
while len(MST) <= V:
    minV = 0xfffffff
    min_idx = 0
    for i in range(V+1):
        if i not in MST and cost[i] < minV:
            min_idx = i
            minV = cost[i]
    # 반복문을 다 돌고 나면, 최소 비용으로 갈 수 있는 노드가 선택됨
    # 선택된 노드를 MST에 추가하고,
    # 그 노드로부터 다른 노드로 갈 수 있는 비용을 확인하고(인접한 노드들의 가중치 확인),
    # 기존 비용보다 더 적다면 업데이트 해 주기!

    # 선택된 노드 MST에 추가부터 하자!
    MST.add(min_idx)
    MST_value += minV

    # 비용 확인 후 업데이트 해 주기
    for i in range(V+1):
        if i not in MST and adj[min_idx][i] and adj[min_idx][i] < cost[i]:
            cost[i] = adj[min_idx][i]

print(MST_value)
