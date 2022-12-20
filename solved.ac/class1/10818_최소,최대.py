# N개의 정수가 주어질 때 최솟값과 최댓값을 공백으로 구분해 출력

N = int(input())
number = list(map(int, input().split()))    # number : list
max = max(number)
min = min(number)
print(min, max)
