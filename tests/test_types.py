import pytest
from faker import Faker
from tablefiller import *

# Test for Int generator (тесты для генерации целых чисел)
def test_int_generator():
    int_gen = Int(2, 5)
    value = int_gen.generate()
    assert isinstance(value, int)
    assert 2 <= value <= 5

def test_int_value_exception():
    with pytest.raises(ValueError):
        Int(5, 2)

def test_int_type_exception():
    with pytest.raises(TypeError):
        Int('a', 3)
        Int(1, 'a')

# Test for Float generator (тесты для генерации дробных чисел)

def test_float_type_exception():
    with pytest.raises(TypeError):
        Float("a", 4, 4)
        Float(1, "a", 4)
        Float(1, 4, "a")
        Float(1, 4, 1.2)

def test_float_value_exception():
    with pytest.raises(ValueError):
        Float(4, 1, 4)
        Float(1, 4, -2)

def test_float_generator():
    float_gen = Float(1, 4, 4)
    value = float_gen.generate()
    assert isinstance(value, float)
    assert 1 <= value <= 4

# Test for Str generator (тесты для генерации строк)

def test_string_type_exception():
    with pytest.raises(TypeError):
        Str("a")
        Str(1.4)

def test_string_value_exception():
    with pytest.raises(ValueError):
        Str(-1)

def test_string_generator():
    test_str, size = "TEST", 5
    str_gen = Str(size, test_str)
    value = str_gen.generate(fake=Faker("ru_RU"))
    assert isinstance(value, str)
    assert value[:4] == test_str
    assert len(value) == len(test_str) + size

# Test for Date generator (тесты для генерации даты)

def test_date_type_exception():
    with pytest.raises(TypeError):
        Date(1, '01.01.2001', '%d.%m.%Y')
        Date('01.01.2001', 2.4, '%d.%m.%Y')
        Date('01.01.2001', '01.01.2001', 0)

def test_date_value_exception():
    with pytest.raises(ValueError):
        Date('01.01.2001', '01.02.2001', '%Y.%m.%d')
        Date('01.03.2001', '01.02.2001', '%d.%m.%Y')
        
def test_date_generator():
    start_date, end_date = '01.01.2025', '01.02.2025'
    data_gen = Date(start_date, end_date, '%d.%m.%Y')
    value = data_gen.generate()
    assert isinstance(value, str)
    assert datetime.strptime(value, '%Y-%m-%d')

# Test for Category generator (тесты для категориальных данных)

def test_category_value_exception():
    with pytest.raises(ValueError):
        Category([])

def test_category_generator():
    categories = ['A', 'B', 'C']
    cat_gen = Category(categories)
    value = cat_gen.generate()
    assert isinstance(value, str)
    assert value in categories

# Test for Job generator (тесты для генерации работ)

def test_job_type_exception():
    with pytest.raises((TypeError, AttributeError)):
        Job([]).generate(Faker("ru_RU"))
        Job(3).generate(Faker("ru_RU"))
        Job(3.2).generate(Faker("ru_RU"))

def test_job_value_exception():
    with pytest.raises(ValueError):
        Job('invalid_type').generate(Faker("ru_RU"))

def test_job_generator():
    job_types = ['male', 'female', 'both']
    fake = Faker('ru_RU')
    for type in job_types:
        job_gen = Job(type)
        value = job_gen.generate(fake)
        assert isinstance(value, str)
        assert len(value) > 0

# Test for Phone generator (тесты для генерации номеров телефона)

def test_phone_generator():
    phone_gen = Phone()
    fake = Faker('ru_RU')
    value = phone_gen.generate(fake)
    assert isinstance(value, str)
    assert len(value) > 0

# Test for Email generator (тесты для генерации электронных почт)

def test_email_type_exception():
    with pytest.raises((TypeError, AttributeError)):
        Email([]).generate(Faker("ru_RU"))
        Email(3).generate(Faker("ru_RU"))
        Email(3.2).generate(Faker("ru_RU"))

def test_email_value_exception():
    with pytest.raises(ValueError):
        Email('invalid_type').generate(Faker("ru_RU"))

def test_email_generator():
    email_types = ['email', 'free', 'company']
    fake = Faker('ru_RU')
    for type in email_types:
        email_gen = Email(type)
        value = email_gen.generate(fake)
        assert isinstance(value, str)
        assert '@' in value
        assert '.' in value

# Test for Name generator (тесты для генерации имен)

def test_name_type_exception():
    with pytest.raises((TypeError, AttributeError)):
        Name([]).generate(Faker("ru_RU"))
        Name(3).generate(Faker("ru_RU"))
        Name(3.2).generate(Faker("ru_RU"))

def test_name_value_exception():
    with pytest.raises(ValueError):
        Name('invalid_type').generate(Faker("ru_RU"))

def test_name_generator():
    name_types = ['male', 'female', 'both']
    fake = Faker('ru_RU')
    for type in name_types:
        name_gen = Name(type)
        value = name_gen.generate(fake)
        assert isinstance(value, str)
        assert len(value) > 0


# Test for Address generator (тесты для генерации адресов)

def test_for_type_exception():
    with pytest.raises((TypeError, AttributeError)):
        Address([]).generate(Faker("ru_RU"))
        Address(3).generate(Faker("ru_RU"))
        Address(3.2).generate(Faker("ru_RU"))

def test_address_value_exception():
    with pytest.raises(ValueError):
        Address('invalid_type').generate(Faker("ru_RU"))

def test_address_generator():
    address_types = ['street', 'city', 'full']
    fake = Faker('ru_RU')
    for type in address_types:
        addr_gen = Address(type)
        value = addr_gen.generate(fake)
        assert isinstance(value, str)
        assert len(value) > 0