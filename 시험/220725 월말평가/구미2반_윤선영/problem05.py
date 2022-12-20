# 비밀번호 : 8자 이상 32자 이하
# 범위 만족하면 True, 아니면 False 반환

def check_password_length(password):
    if len(password) >= 8 and len(password) <= 32:
        return True
    else:
        return False


# print(check_password_length('01234567890123456789012345678901'))
