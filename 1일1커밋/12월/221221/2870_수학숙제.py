# 숫자 + 알파벳 소문자 -> 숫자를 모두 찾아 비내림차순으로 정리
# 숫자 앞에 0이 있는 경우 생략 가능
import sys

N = int(sys.stdin.readline().strip())
for _ in range(N):
    word = sys.stdin.readline().strip()
    
