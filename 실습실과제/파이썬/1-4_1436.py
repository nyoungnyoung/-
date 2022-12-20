# 1000미만의 자연수에서 2,7의 배수의 총합을 구해라
set_2 = {i for i in range(1000) if i % 2 == 0}
set_7 = {i for i in range(1000) if i % 7 == 0}
set_27 = list(set_2 | set_7)
print(sum(set_27))

# 교수님 코드
sum_num = 0                         # 초기화 굉장히 중요하다는 거 잊지 말기!!
for num in range(1,1000):
    if num % 2 == 0 or num % 7 == 0:   
        sum_num += num
print(sum_num)