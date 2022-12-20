x, y, w, h = map(int, input().split())
# 위 / 오른쪽 / 아래 / 왼쪽
len_lst = [h - y, w - x, x, y]
print(min(len_lst))
