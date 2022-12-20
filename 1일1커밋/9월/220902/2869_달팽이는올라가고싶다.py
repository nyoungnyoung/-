# V : 나무막대 높이 / A : 아침에 올라가는 높이 / B : 미끄러지는 높이
# V - A : 달팽이가 올라가야하는 높이 A - B : 하루에 올라가는 높이
import math
A, B, V = map(int, input().split())
print(math.ceil((V-A)/(A-B))+1)