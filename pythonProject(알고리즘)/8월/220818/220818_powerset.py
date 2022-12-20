arr = [1, 2, 3, 4]
# 첫번째 요소의 부분집합 포함여부를 0과 1로 표현
for i in range(2):      # i 가 0번요소의 부분집합 포함여부 결정
    for j in range(2):
        for k in range(2):
            for l in range(2):
                status = [i, j, k, l]
                for idx in range(len(status)):
                    if status[idx]:
                        print(arr[idx], end=' ')
                print()