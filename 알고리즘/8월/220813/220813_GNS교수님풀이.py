import sys
sys.stdin = open()


# 문자열 크기비교로는 정렬 불가능하니까
# 각 문자열의 크기를 비교할 수 있는 방안이 필요하다!
# 각 문자열의 value를 가지고 있는 dictionary를 이용하면 크기 비교 가능


# 정렬 함수 하나 만들어주자!
def GNS_sort(arr):
    GNS_value = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    # arr 정렬하기 : 버블정렬
    # 요소 2개 비교해서 큰값 뒤로 보내기
    # 큰 원소를 뒤로 보내는 작업 * N번 수행
    for j in range(N-1):
        # 가장 앞쪽 원소부터 제일 뒤 원소까지 2개씩 비교해서 큰 값 뒤로 보내기
        for i in range(N-1-j):
            if GNS_value[arr[i]] > GNS_value[i+1]:      # 앞쪽요소가 뒤쪽요소보다 크면
                arr[i], arr[i+1] = arr[i+1], arr[i]

# 카운팅 정렬 이용
def GNS_sort2(arr):
    GNS_value = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    # 각 요소가 몇 번 나왔는지 숫자세기
    # 누적합 구하기(요소 몇번째 자리에 들어가야 하는지 위치 구하기)
    # 요소들을 위치보고 복사하면 됩니다.
    K = 10
    counts = [0] * K
    sorted_arr = [''] * N
    for i in range(N):
        # 여기서 글로벌 N의 값을 변경하고 싶다면
        # global N 선언해주고 변경해야함
        # 값을 가져와서 사용만 할거라면 필요없다!
        index = GNS_value[arr[i]]
        counts[index] += 1
    for i in range(1, K):
        counts[i] += counts[i-1]
    # 새로운 배열에 요소가 들어갈 위치에 값을 복사
    for i in range(N):
        # arr[i]요소가 들어갈 자리(counts[GNS_value[arr[i]]])에다가 넣어주기
        counts[GNS_value[arr[i]]] -= 1
        sorted_arr[counts[GNS_value[arr[i]]]] = arr[i]
    return sorted_arr

T = int(input())
for _ in range(T):
    tc, N - input().split()
    N = int(N)
    # GNS 숫자 배열 입력받기
    arr = input().split()
    # GNS_sort(arr)
    result = GNS_sort2(arr)
    print(f'{tc}')
    # print(*arr)
    print(*result)     # 배열 이름앞에 * 붙이면 요소만 출력 됨
