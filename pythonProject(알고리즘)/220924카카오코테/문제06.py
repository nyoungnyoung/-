def solution(n, m, x, y, r, c, k):
    delta = {l: (0, -1), r: (0, 1), u: (-1, 0), d: (1, 0)}
    answer = ''
    maze = [[0] * (m+1) for _ in range(n+1)]

    return answer