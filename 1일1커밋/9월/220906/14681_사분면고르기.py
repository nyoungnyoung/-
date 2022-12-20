import sys
def quadrant(x, y):
    if x > 0:
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3


x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
print(quadrant(x, y))
