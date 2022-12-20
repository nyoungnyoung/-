'''
0번부터 N번까지, E개의 간선
6 8     # N E
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6
'''

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
print(adjList)