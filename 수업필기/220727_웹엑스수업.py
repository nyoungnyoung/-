import random
# 로또 번호 생성하는 프로그램 작성(절차지향 프로그래밍)

# 로또 번호를 저장하는 변수(리스트)
# 숫자 6개를 뽑아 낼건데... 중복되지 않는 걸로 >> 6개 뽑는거 한번에
# 랜덤한 숫자를 하나씩 6번 뽑는걸로

lotto_nums = []

# 중복이 나오면 다시 뽑아야 함
# 숫자 6개를 뽑을 때 까지 반복

while len(lotto_nums) < 6:
    num = random.choice(range(1, 46))  # 이 작업을 6번 해야함
    # 중복 되지 않으면 추가하기
    if num in lotto_nums:
        continue  # 중복이면 추가하지 않음
    lotto_nums.append(num)

###################################################

# 똑같은 걸 객체지향 프로그래밍으로 해결해보자!
# 로또 번호 생성 프로그램 작성이라는 목표는 같음


class LottoNumberMaker:
    # 얘가 해야하는 일 >> 로또 번호 생성, 로또 번호 출력
    # 얘가 가지고 있어야 하는 데이터 >> 생성된 로또 번호

    def __init__(self):
        # self.변수명 내가 가지고 있어야할 데이터를 선언
        self.lotto_nums = []

    def print_nums(self):
        print(self.lotto_nums)
    # 객체가 해야하는 일은 메서드(함수)로 선언

    def make_lotto_nums(self):
        while len(self.lotto_nums) < 6:
            num = random.choice(range(1, 46))   # 이 작업을 6번 반복해야함
            if num in self.lotto_nums:
                continue        # 중복이면 추가하지 않음
            # 중복되지 않으면 추가!
            self.lotto_nums.append(num)


###########여기까지는 그냥 클래스만 선언한거.. 실제로 동작하지 않음#####
# 이제부터 로또 번호 생성하는 프로그램을 작성할 거!!
# 해야할 일 >>> 로또 번호 만들어 내는 기계가 있어야 함
lottoMaker1 = LottoNumberMaker()
lst = []
# 위 두가지 작업은 똑같은 작업이라고 보면 됨! 다른 건 타입 뿐
# lst라는 건 빈 리스트의 주솟값을 참조하고 있는 변수
# lottoMaker1은 LottoNumberMaker()의 주솟값을 참조하고 있는 변수
# lottoMaker1과 lst는 둘다 객체이다
# lottoMaker1은 LottoNumberMaker의 인스턴스이고
# lst는 리스트의 인스턴스임!


# 기계를 만들었으니 이제 번호 만들라고 일 시킴
lottoMaker1.make_lotto_nums()
# 번호 만들었으니까 출력하기
lottoMaker1.print_nums()

lottoMaker2 = LottoNumberMaker()
# 두개의 기계를 만들 수도 있음! 1번 기계랑 2번 기계는 다르다!
lottoMaker2.make_lotto_nums()
