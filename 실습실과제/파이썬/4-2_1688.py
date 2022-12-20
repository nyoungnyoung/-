students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

# Dictionary = {이름:득표수, 이름:득표수, 이름:득표수} 이렇게 사용하면 될듯
# 개수를 세서 저장할 빈 dictionary 만들기
# for문 사용해서 리스트의 원소를 하나씩 가져와서 dict의 key값에 있으면
# +1, 없으면 key값에 등록하고 1을 value로 입력

counts = {}

for i in students:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

print(counts)