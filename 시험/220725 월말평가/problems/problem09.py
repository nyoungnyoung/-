# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    if M == 0:                  # 입력값이 0, 위로
        if position[0] == 0:    # 캐릭터가 첫번째 줄에 있을 때
            return False        # 범위 벗어남
        else:
            return True         # (position[0]-1, position[1])
    elif M == 1:                    # 입력값이 1, 밑으로
        if position[0] == N - 1:    # 캐릭터가 마지막 줄에 있을 때
            return False            # 범위 벗어남
        else:
            return True             # (position[0]+1, position[1])
    elif M == 2:                # 입력값이 2, 왼쪽으로
        if position[1] == 0:    # 캐릭터가 첫 행에 있을 때
            return False        # 범위 벗어남
        else:
            return True
    elif M == 3:                    # 입력값이 3, 오른족으로
        if position[1] == N - 1:    # 캐릭터가 마지막 행에 있을 때
            return False            # 범위 벗어남
        else:
            return True
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
