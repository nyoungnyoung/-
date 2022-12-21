# S = (R1 + R2) // 2
# R1, S만 알고 있을 때 R2가 몇인지 구해라
R1, S = map(int, input().split())
R2 = S * 2 - R1
print(R2)
