import random
from faker import Faker
fake = Faker()
print(fake.name())

random.seed(7777)
print(random.random())

random.seed(8888)
print(random.random())

fake1 = Faker('ko_KR')
fake1.seed_instance(87654321)

print(fake1.name())

fake2 = Faker('ko_KR')
print(fake2.name())
