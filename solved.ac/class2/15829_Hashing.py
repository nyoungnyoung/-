import sys

L = int(sys.stdin.readline())
word = sys.stdin.readline()
hash_num = 0
for i in range(L):
    hash_num += (ord(word[i]) - 96) * (31 ** i)     # word[i]의 아스키코드값에서 96 빼주면 해당 문자의 고유넘버
print(hash_num % 1234567891)
