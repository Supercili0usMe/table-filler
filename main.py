from src.tablefiller import *

schema = Table(
    columns= {
        'test_int': Int(5, 10),
        'test_float': Float(1, 10, 2),
        'test_str': Str(5, 'Table '),
        'test_date': Date('25.12.2024', '01.01.2025', '%d.%m.%Y'),
        'test_category': Category(['1', '2', '3', 4, '5']),
        'test_job': Job('both'),
        'test_phone': Phone(),
        'test_email': Email('email'),
        'test_name': Name('both'),
        'test_address': Address('full')
    },
    local='ru_RU'
)

generator = DataGenerator(schema)
data = generator.generate_data(15)

data.to_csv('output.csv')
data.to_json('output.json')
data.to_sql('output.sql')