n = int(input())
# line : house
# 1 : 1 (1개)
# 2 : 2~7 (6개)
# 3 : 8~19 (12개)
# 4 : 20~37 (18개)
# 5 : 38~61 (24개)
# 6 : 62~93 (32개)
# ...

house = 1
line = 1
while n > house:
    house += 6 * line   # house 개수 = 1 + 6 * line개수
    line += 1           # line개수 1개씩 증가
print(line)
