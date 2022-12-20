# 크기가 N인 배열의 모든 원소에 접근하는 재귀함수
# 굳이 배열을 재귀로 접근해야해? 라는 생각이 들 수 있겠지만
# 나중에 우리가 재귀를 사용하는 상황들이 보통 배열의 각 원소에 접근하는 동작과
# 연관되어있는 경우가 많다! 그러니까 미리 알아두는게 좋음

def f(i, N):
    if i == N:      # 배열을 벗어남
        return
    else:           # 남은 원소가 있는 경우
        B[i] = A[i]
        # print(A[i])
        f(i+1, N)   # 다음 원소로 이동

N = 3
A = [1, 2, 3]
B = [0] * N
f(0, N)             # 0번 원소부터 N개의 원소에 접근
print(B)