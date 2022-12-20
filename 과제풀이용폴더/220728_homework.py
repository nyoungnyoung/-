# 1번
class Circle:
    pi = 3.14

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return Circle.pi * self.r * self.r

    def circumference(self):
        return 2 * Circle.pi * self.r

    def center(self):
        return (self.x, self.y)


circle1 = Circle(3, 2, 4)
print(circle1.area())
print(circle1.circumference())

# 2번


class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')


class Bird(Animal):
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f'{self.name}! 푸드덕!')


dog = Dog('꼽이')
dog.run()  # 꼽이! 달린다!
dog.bark()  # 꼽이! 짖는다!
bird = Bird('구구')
bird.walk()  # 구구! 걷는다!
bird.eat()  # 구구! 먹는다!
bird.fly()  # 구구! 푸드덕!
