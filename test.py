# print("\033[3m\033[33m\033[41m{}\033[0m".format("Hello world"))
# from faker import Faker

# fake = Faker("ru_RU")
# print(fake.job())
# print(fake.phone_number())
# print(fake.hostname())
# print(fake.ascii_free_email())
# print(fake.uri())
# print(fake.company())
# print(fake.pystr())


# a = [i for i in range(25)]
# res = []
# for i in range(0, len(a), 10):
#     res.append(a[i:i+10 if i+10 < len(a) else len(a)])
# print(res)

# args = ('male', 'female', 'both')

# print(f"{", ".join(args)}")
from tablefiller import *
from tablefiller.generator import DataGenerator

pop = Table(columns= {'int': Int(11, 80),
                      'reshetka': Float(11, 80, 1),
                      'jfpoweij': Str(12, ' '),
                      'woerhiuf': Date('01.01.1488', '13.09.1488', '%d.%m.%Y'),
                      'wojief': Category(['3']),
                      'wef': Job('both'),
                      'weiojnf': Phone(),
                      'qwehjoif': Email('email'),
                      'owiernhg': Name('both'),
                      'oijhwegf': Address('full')}
                      )

generator = DataGenerator(pop)
data = generator.generate_data(15)

generated_data = GeneratedData([
        {"name": "Test Name", "age": 25, "email": "test@email.com"},
        {"name": "Test Name 2", "age": 30, "email": "test2@email.com"}
    ])
generated_data.to_csv('invalid/path/test.csv')