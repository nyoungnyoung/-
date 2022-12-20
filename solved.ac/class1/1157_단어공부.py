import sys
word = sys.stdin.readline().rstrip().upper()
alp = list(set(word))
lst = []
for i in alp:
    lst.append(word.count(i))
if lst.count(max(lst)) >= 2:
    print('?')
else:
    print(alp[lst.index(max(lst))])

# zZa : max(lst) = 2
# alp : 중복제외 알파벳리스트
# lst : alp의 등장횟수리스트
# lst에서 max(lst) 인덱스 찾아서 alp[인덱스] 출력