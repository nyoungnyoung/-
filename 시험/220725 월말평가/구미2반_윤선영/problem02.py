# 전체 점수의 평균을 게산하는 함수 average
# 평균점수 = 전체 점수의 합 / 점수의 개수
# 점수의 합은 sum으로, 개수는 len으로

def average(score):
    return sum(score)//len(score)


# print(average([80, 90, 85, 75]))
