# 최댓값
# import sys
# N = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# max_val = arr[0]    # 첫 원소를 최대값으로 가정
# for i in range(1, N):       # 나머지 모든 원소에 대해
#     if arr[i] > max_val:
#         max_val = arr[i]
#
# print(max_val)

# 최댓값의 위치 출력, 같은 값이 있을 때는 맨 오른쪽
# import sys
# N = int(sys.stdin.read())
# arr = list(map(int, sys.stdin.readline()))
# maxIdx = 0   # 가정
# for i in range(1, N):
#     if arr[maxIdx] <= arr[i]:
#         maxIdx = i
# print(maxIdx)

# 버블 소트
# N = int(input())
# arr = list(map(int, input().split()))
# for i in range(N-1, 0, -1):  # 구간의 맨 끝 인덱스 정하기
#     for j in range(i):  # 인접 원소 중 왼쪽원소의 인덱스
#         if arr[j] > arr[j+1]:   # 오름차순, 더 큰수를 오른쪽으로
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# 카운트 정렬
N = int(input())
arr = list(map(int, input().split()))
c = [0] * 101   # 0부터 100까지 숫자 개수, 인덱스가 100까지 있어야 하니까 101개
tmp = [0] * N   # 정렬된 배열
for i in range(N):  # 카운트배열 만드는 방법
    c[arr[i]] += 1
for i in range(1, 101):  # 개수 누적
    c[i] += c[i-1]
for i in range(N-1, -1, -1):    # 원본 데이터를 뒤에서부터 읽으면서 정렬 결과를 tmp에 저장
    c[arr[i]] -= 1
    tmp[c[arr[i]]] = arr[i]
print(tmp)
