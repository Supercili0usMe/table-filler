import random
from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class DataType(ABC):
    """Base abstract class for all data types.
    Базовый абстрактный класс для всех типов данных."""

    @abstractmethod
    def generate(self):
        raise NotImplementedError

class Int(DataType):
    """Generates integer values within specified range.
    Генерирует целые числа в указанном диапазоне.

    Args:
        `min_value` (int): Lower bound / Нижняя граница
        `max_value` (int): Upper bound / Верхняя граница"""
    
    def __init__(self, min_value: int, max_value: int):
        if max_value <= min_value:
            raise ValueError(f"Нижняя граница должна быть меньше верхней границы, а сейчас '{max_value = }' <= '{min_value = }'")
        self.max_value = max_value
        self.min_value = min_value
            
    
    def generate(self):
        return random.randint(self.min_value, self.max_value)

class Float(DataType):
    """Generates float values within specified range.
    Генерирует дробные числа в указанном диапазоне.

    Args:
        `min_value` (int | float): Lower bound / Нижняя граница
        `max_value` (int | float): Upper bound / Верхняя граница
        `precision` (int): Decimal places / Знаков после запятой"""
    
    def __init__(self, min_value: int | float, max_value: int | float, precision: int):
        if max_value <= min_value:
            raise ValueError(f"Нижняя граница должна быть меньше верхней границы, а сейчас '{max_value}' <= '{min_value}'")
        if precision <= 0:
            raise ValueError(f"Количество знаков после запятой должно быть положительным, а сейчас '{precision}'")
        
        self.max_value = max_value
        self.min_value = min_value
        self.precision = precision
            
    
    def generate(self):
        return round(random.uniform(self.min_value, self.max_value), self.precision)

class Str(DataType):
    """Generates string values with optional prefix.
    Генерирует строковые значения с опциональным префиксом.

    Args:
        `length` (int): Max string length / Максимальная длина
        `prefix` (str, optional): String prefix / Префикс строки"""
    def __init__(self, length: int, prefix: str = ""):
        if length <= 0:
            raise ValueError("Длина не может быть отрицательной")
        self.length = length
        self.prefix = prefix
    
    def generate(self, fake):
        return fake.pystr(max_chars=self.length, prefix=self.prefix)

class Date(DataType):
    """Generates dates within specified range.
    Генерирует даты в указанном диапазоне.

    Args:
        `start_date` (str): Start date / Начальная дата
        `end_date` (str): End date / Конечная дата
        `format` (str): Date format / Формат даты"""
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
    """Generates values from predefined categories.
    Генерирует значения из предопределенных категорий.

    Args:
        `categories` (list): Available categories / Доступные категории"""
    def __init__(self, categories: list):
        if not categories:
            raise ValueError("Список категорий не может быть пустым")
        self.categories = categories
    
    def generate(self):
        return random.choice(self.categories)

class Job(DataType):
    """Generates job titles.
    Генерирует названия профессий.

    Args:
        `type` (str): 'male', 'female' or 'both'"""
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
    """Generates phone numbers.
    Генерирует номера телефонов."""
    def generate(self, fake):
        return fake.phone_number()

class Email(DataType):
    """Generates email addresses.
    Генерирует адреса электронной почты.

    Args:
        `type` (str): 'email', 'free' or 'company'"""
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
    """Generates person names.
    Генерирует имена.

    Args:
        `type` (str): 'male', 'female' or 'both'"""
    
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
    """Generates addresses.
    Генерирует адреса.
    
    Args:
        `type` (str): 'street', 'city' or 'full'"""
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