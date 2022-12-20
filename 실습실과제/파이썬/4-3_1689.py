# list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남기고 제거한 list를 출력
# 이 때 제거된 후 남은 수들이 담긴 list의 요소들은 기존 순서를 유지해야함

# 일단 input형태는 1 1 3 3 이런식으로 입력되는걸로 가정하자
# 빈 새 리스트를 하나 만들어두고 반복문 수행하면서 lst의 인덱스가 새 리스트
# 마지막 인덱스와 같으면 넘어가고, 같지않으면 새 리스트에 해당 문자열 추가

lst = input().split()
result = []
print(lst)
print(range(len(lst)))
for i in range(len(lst)):
    if i == 0:
        result.append(lst[i])
    elif lst[i] != result[-1]:
        result.append(lst[i])

print(result)