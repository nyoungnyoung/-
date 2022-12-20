# 일단 나는 시험만 볼거야! 라는 마음으로 공부하기
# 상속
class Shape:        # 부모 클래스(super class)

    def __init__(self):
        self.name = '도형'
        self.area = 0

    def draw(self):
        print(f'{self.name}을 그립니다.')


# 사각형, 원

class Rectangle(Shape):     # Shape 클래스 상속
    
    # 가로, 세로
    def __init__(self, width, height):
        # 부모 클래스의 생성자 호출하기
        # 자식 클래스 내에서 부모 클래스를 지칭할 때
        # super 키워드 사용
        super().__init__()
        self.width = width
        self.height = height
    # 너비 계산하기
    def cal_area(self):
        self.area = self.width * self.height

    # draw 재정의 : 부모 클래스에 정의된 메서드랑 똑같이 만들면 됨
    def draw(self):
        print('직선을 그립니다')
        print('직선을 그립니다')
        print('직선을 그립니다')
        print('직선을 그립니다')
        print('사각형을 그렸습니다')

class Circle(Shape):
    pi = 3.14
    def __init__(self, radious):
        super().__init__()
        self.radious = radious
    # 너비 계산하기
    def cal_area(self):
        self.area = self.radious**2 * Circle.pi
    
    def draw(self):
        print('곡선을 그립니다')
        print('원을 그렸습니다')


rect1 = Rectangle(5,10)     # Rectangle 클래스 인스턴스 생성
# 상속을 하면 기존 클래스의 특징을 그대로 사용 가능
# rect1.area = 100
rect1.name = '사각형'
rect1.draw()

cir1 = Circle(5)
# cir1.area = 50
cir1.name = '원'
cir1.draw()

# 부모가 가진 메서드를 자식클래스에서
# 자식클래스에 맞게 변경해서 사용할 수 있음
# 메서드 재정의(method override)

# 자바 : 메서드 오버로딩 vs 메서드 오버라이딩
# 메서드 오버라이딩은 필수요건이 상속관계여야 한다는 것
# 오버로딩 : 이름이 똑같은 메서드를 여러개 정의하는 것
# 근데... 파이썬은 오버로딩이 안됩니다! 

# 오버로딩의 조건 : 매개변수의 타입, 개수, 순서가 달라야 함
# 근데 파이썬은 변수의 타입지정이 없음 >>> 오버로딩 안됨


# draw_shape만든 사람이... 인자로 shape를 받는다고 가정하고..만듬
def draw_shape(shape):
    shape.draw()            # 똑같은 코드인데

draw_shape(rect1)           # 인자가 다르게 들어오니까 결과가 다름!
draw_shape(cir1)            # 이게 '다형성'


# 캡슐화 : 외부에서 내부의 내용을 알지 못하게 하는 것
# 클래스를 제공해주면 클래스를 사용하는 사람들은 내부가 어떻게
# 구현되었는지 몰라도 메서드를 잘 사용할 수 있음
# 명세서만 제공해주면 외부에서 클래스 내부에 선언된 변수나 메서드에
# 접근 할 수 있는 권한을 줌으로써, 개발자가 허용한 변수
# 및 메서드에만 접근할 수 있음
