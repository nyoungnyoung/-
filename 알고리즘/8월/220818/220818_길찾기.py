import sys
sys.stdin = open('길찾기_input.txt', 'r')

def dfs(s, g):
    stack = []
    visited[s] = 1                  # 시작점 방문표시
    stack.append(s)                 # stack에 s push
    while stack:                    # stack 안에 요소가 있는 동안 반복(스택이 빌때까지)
        start = stack.pop()         # 시작점을 stack의 마지막 요소로 설정
        for w in arr[start]:        # 시작점과 연결되어있는 노드 w를 탐색할건데
            if visited[w] == 0:     # w에 방문한적이 없으면
                if w == g:          # 만약 g에 방문하는 즉시
                    return True     # True값 반환
                visited[w] = 1
                stack.append(w)
    return False                    # while문 종료되면 False값 반환

for _ in range(10):
    T, N = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [[] for _ in range(100)]
    visited = [0] * 100
    # lst 의 요소에 2칸씩 띄어서 접근 하며 arr 완성
    for i in range(0, len(lst), 2):
        a, b = lst[i], lst[i+1]
        arr[a].append(b)
    result = int(dfs(0, 99))
    print(f'#{T} {result}')