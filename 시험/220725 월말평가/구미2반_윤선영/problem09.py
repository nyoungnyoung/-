# 입력값(m) 기준으로 함수 작성

def is_position_safe(n, m, position):
    if m == 0:                  # 입력값이 0, 위로
        if position[0] == 0:    # 캐릭터가 첫번째 줄에 있을 때
            return False        # 범위 벗어남
        else:
            return True         # (position[0]-1, position[1])
    elif m == 1:                    # 입력값이 1, 밑으로
        if position[0] == n - 1:    # 캐릭터가 마지막 줄에 있을 때
            return False            # 범위 벗어남
        else:
            return True             # (position[0]+1, position[1])
    elif m == 2:                # 입력값이 2, 왼쪽으로
        if position[1] == 0:    # 캐릭터가 첫 행에 있을 때
            return False        # 범위 벗어남
        else:
            return True
    elif m == 3:                    # 입력값이 3, 오른족으로
        if position[1] == n - 1:    # 캐릭터가 마지막 행에 있을 때
            return False            # 범위 벗어남
        else:
            return True


# print(is_position_safe(3, 1, (0, 0)))
# print(is_position_safe(3, 1, (2, 0)))
