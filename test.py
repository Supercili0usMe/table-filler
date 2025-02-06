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
from src.tablefiller import *

pop = Table(columns= {'int': Int(11),
                      'reshetka': Float(5, 1),
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

data.to_csv('output.csv')
data.to_json('output.json')
data.to_sql('output.sql')
print(data)