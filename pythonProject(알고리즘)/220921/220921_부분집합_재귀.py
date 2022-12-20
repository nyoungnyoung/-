# 부분집합을 재귀로 구현
def powerset(i, k):
    if i == k:
        # print(bit)
        for j in range(k):
            if bit[j]:      # bit[j] == 1이면
                print(arr[j], end=' ')
        print()
    else:
        bit[i] = 0
        powerset(i+1, k)
        bit[i] = 1
        powerset(i+1, k)

arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

bit = [0] * n       # bit[i] : arr[i]가 부분집합의 원소인지 표시
powerset(0, n)