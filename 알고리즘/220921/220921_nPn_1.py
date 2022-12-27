# 교재 p.28 단순 for문 돌려서 순열 생성하는 방법
for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            for k in range(1, 4):
                if k != i and k != j:
                    print(i, j, k)