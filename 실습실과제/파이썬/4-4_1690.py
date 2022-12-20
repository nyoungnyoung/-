# ord(str) : str을 아스키코드로 변환함
# sum_ord 변수 : word의 길이만큼 반복문 수행 & 
# word의 인덱스를 아스키코드로 변환한 수를 차곡차곡 더해주자

word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')
sum_ord1 = 0
sum_ord2 = 0

for i in word1:
    sum_ord1 += ord(i)
for j in word2:
    sum_ord2 += ord(j)

if sum_ord1 > sum_ord2:
    print(word1)
elif sum_ord1 < sum_ord2:
    print(word2)
else:
    print(word1,word2)