import random
from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class DataType(ABC):
    """Базовый класс для всех типов данных."""
    @abstractmethod
    def generate(self):
        raise NotImplementedError

class Int(DataType):
    """Класс для работы с целочисленным типом данных.
    ----
    Параметры:
        - `min_value` - нижняя граница для генерации.
        - `max_value` - верхняя граница для генерации.
    """
    def __init__(self, min_value: int, max_value: int):
        if max_value <= min_value:
            raise ValueError(f"Нижняя граница должна быть меньше верхней границы, а сейчас '{self.max_value}' <= '{self.min_value}'")
        self.max_value = max_value
        self.min_value = min_value
            
    
    def generate(self):
        return random.randint(self.min_value, self.max_value)

class Float(DataType):
    """Класс для работы с дробными числами.
    ----
    Параметры
       - `min_value` - нижняя граница для генерации.
       - `max_value` - верхняя граница для генерации.
       - `precision` - количество символов после запятой."""
    def __init__(self, min_value: int, max_value: int, precision: int):
        if max_value <= min_value:
            raise ValueError(f"Нижняя граница должна быть меньше верхней границы, а сейчас '{self.max_value}' <= '{self.min_value}'")
        if precision <= 0:
            raise ValueError(f"Количество знаков после запятой должно быть положительным, а сейчас '{self.precision}'")
        
        self.max_value = max_value
        self.min_value = min_value
        self.precision = precision
            
    
    def generate(self):
        return round(random.uniform(self.min_value, self.max_value), self.precision)

class Str(DataType):
    """Класс для работы со строковыми данными.
    ----
    Параметры:
        - `length` - максимальная длина для генерации строки,
        - `prefix` - префикс, который добавляется в начало строк. Например, 
        если вы хотите, чтобы происходила генерация названий товаров, например `'Товар фывлод'`,
        то необходимо указать в качестве префикса `'Товар'`."""
    def __init__(self, length: int, prefix: str =None):
        if length <= 0:
            raise ValueError("Длина не может быть отрицательной")
        self.length = length
        self.prefix = prefix
    
    def generate(self, fake):
        return fake.pystr(max_chars=self.length, prefix=self.prefix)

class Date(DataType):
    """Класс для работы с датами.
    ----
    Параметры:
        - `start_date` - начальная дата, от которой будет происходить генерация,
        - `end_date` - конечная дата, до которой будет происходить генерация,
        - `format` - формат, в котором подаются даты."""
    def __init__(self, start_date: str, end_date : str, format: str):
        try:
            self.start_date = datetime.strptime(start_date, format)
            self.end_date = datetime.strptime(end_date, format)
        except ValueError:
            raise ValueError("Неверный формат даты.")
        
        if self.end_date <= self.start_date:
            raise ValueError("Конечная дата должна быть позже начальной")
    
    def generate(self):
        random_date = self.start_date + timedelta(days=random.randint(0, (self.end_date - self.start_date).days))
        return random_date.strftime('%Y-%m-%d')

class Category(DataType):
    """Класс для работы с категориальными данными.
    ----
    Параметры:
        - `categories` - список категорий, из которых необходимо выбирать данные."""
    def __init__(self, categories: list):
        if not categories:
            raise ValueError("Список категорий не может быть пустым")
        self.categories = categories
    
    def generate(self):
        return random.choice(self.categories)

class Job(DataType):
    """Класс для генерации рабочего места.
    ----
    Параметры:
        - `type` - тип категории работы (`'male'`, `'female'`, `'both'`)."""
    def __init__(self, type: str):
        self.__args = ('male', 'female', 'both')
        self.type = type.lower()
        
    def generate(self, fake):
        if self.type == 'male':
            return fake.job_male()
        elif self.type == 'female':
            return fake.job_female()
        elif self.type == 'both':
            return fake.job()
        else:
            raise ValueError(f"Такого аргумента нету. Возможные аргументы: {", ".join(self.__args)}")

class Phone(DataType):
    """Класс для генерации номера телефона.
    ----"""
    def generate(self, fake):
        return fake.phone_number()

class Email(DataType):
    """Класс для генерации адресов электронных почт.
    ----
    Параметры:
        - `type` - тип генерируемых почт (`'email'`, `'free'`, `'company'`)"""
    def __init__(self, type: str):
        self.__args = ('email', 'free', 'company')
        self.type = type.lower()

    def generate(self, fake):
        if self.type == 'email':
            return fake.email()
        elif self.type == 'free':
            return fake.free_email()
        elif self.type == 'company':
            return fake.company_email()
        else:
            raise ValueError(f"Такого аргумента нету. Возможные аргументы: {", ".join(self.__args)}")

class Name(DataType):
    """Класс для генерации случайных имен.
    ----
    Параметры:
        - `type` - тип генерируемых имен (`'male'`, `'female'`, `'both'`)"""
    
    def __init__(self, type: str):
        self.__args = ('male', 'female', 'both')
        self.type = type.lower()
    
    def generate(self, fake):
        if self.type == 'male':
            return fake.name_male()
        elif self.type == 'female':
            return fake.name_female()
        elif self.type == 'both':
            return fake.name()
        else:
            raise ValueError(f"Такого аргумента нету. Возможные аргументы: {", ".join(self.__args)}")

class Address(DataType):
    """Класс для генерации случайных адресов.
    ----
    Параметры:
        - `type` - тип генерируемого адреса (`'street'`, `'city'`, `'full'`)"""
    def __init__(self, type: str):
        self.__args = ('street', 'city', 'full')
        self.type = type.lower()

    def generate(self, fake):
        if self.type == 'street':
            return fake.street_address()
        elif self.type == 'city':
            return fake.city()
        elif self.type == 'full':
            return fake.address()
        else:
            raise ValueError(f"Такого аргумента нету. Возможные аргументы: {", ".join(self.__args)}")