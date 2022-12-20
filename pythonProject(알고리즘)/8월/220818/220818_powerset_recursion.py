# 재귀는 같은 모양을 반복호출하는 것 >> 반복문처럼 보일 수 있지만
# 특정한 함수 내부에서 똑같이 생긴 함수를 호출하는 것

def powerset(idx, status):
    if idx == N:
        print(status)
        return                      # 더이상 재귀 호출 하지 마라! return : 함수 종료
    for i in range(2):              # 반복문 안에서
        status[idx] = i
        powerset(idx + 1, status)   # 반복문이 또 돌고있다고 생각하면 됨(근데 재귀로 호출한거)
    # 함수 마지막 줄에는 항상 return이 숨어 있음
    # return == return None

N = 4
status = [0] * N
powerset(0, status)
