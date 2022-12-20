score = {'python': 80, 'django': 89, 'web': 83}
score['algorithm'] = 90
score['python'] = 85
sum_score = sum(score.values())
print(sum_score / 4)

# 교수님 코드
score = {'python': 80, 'django': 89, 'web': 83}
# 알고리즘 90점 추가, python 85점 변경
score['algorithm'] = 90
score['python'] = 85
total_score = 0
for key in score.keys():
    total_score += score.get(key)
print(total_score / len(score))