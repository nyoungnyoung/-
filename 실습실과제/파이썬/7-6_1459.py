class Doggy:                    # Doggy 클래스는 이렇습니다!
    num_of_dogs = 0             # 클래스 변수
    birth_of_dogs = 0

    def __init__(self, name, breed):    # 인스턴스 메서드
        self.name = name        # 인스턴스 변수
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def __del__(self):          # 인스턴스 메서드
        Doggy.num_of_dogs -= 1

    def bark(self):             # bark() 메서드 -> 짖는다!
        print('멍멍!')

    @classmethod                # 클래스 메서드
    def get_status(cls):
        print(f'태어난 강아지 수는 {Doggy.birth_of_dogs}마리 입니다.')
        print(f'현재 강아지 수는 {Doggy.num_of_dogs}마리 입니다.')


dog1 = Doggy('마루', '래브라도리트리버')
dog2 = Doggy('우디', '보더콜리')
dog3 = Doggy('뽀삐', '말티즈')
print(dog1.name)
print(dog1.breed)
print(dog2.name)
print(dog2.breed)
print(dog1.bark())
del dog3
Doggy.get_status()
