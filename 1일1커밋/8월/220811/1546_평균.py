import sys
N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
M = max(score)
for s in range(len(score)):
    score[s] = score[s] / M * 100
print(sum(score)/len(score))