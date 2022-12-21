# X가 주어졌을 때, 
# X와 구성이 같으면서 X보다 큰 수 중 가장 작은 수 출력
# 순열 이용하면 쉽게 풀 수 있음!
import sys
from itertools import permutations
X = sys.stdin.readline().strip()
print(permutations(X, len(X)))
lst = list(permutations(X, len(X)))
nums = []
for i in lst:
    num = int(''.join(i))
    if num > int(X) and num not in nums:
        nums.append(num)
        nums.sort()
if nums:
    print(nums[0])
else:
    print(0)

