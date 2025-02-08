import csv, json
from typing import List
from faker import Faker
from .schema import *
from .types import *

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False


class GeneratedData(list):
    """Extended list class for data export functionality.
    Расширенный класс списка с функциями экспорта данных."""
    def __init__(self, data: List[dict]):
        super().__init__(data)
    
    def to_csv(self, file_path: str) -> None:
        """Exports data to CSV file.
        Экспортирует данные в CSV файл.

        Args:
            `file_path` (str): Output file path / Путь к файлу"""
        if not self:
            raise ValueError("Отсутствуют данные для экспорта")
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self[0].keys())
                writer.writeheader()
                writer.writerows(self)
        except OSError as e:
            raise OSError(f"Ошибка в записи файла: {e}")

    def to_json(self, file_path: str) -> None:
        """Exports data to JSON file.
        Экспортирует данные в JSON файл.

        Args:
            `file_path` (str): Output file path / Путь к файлу"""
        if not self:
            raise ValueError("Отсутствуют данные для экспорта")
        try:
            with open(file_path, 'w', encoding='utf-8') as jsonfile:
                json.dump(self, jsonfile, indent=4, ensure_ascii=False)
        except OSError as e:
            print(f"Ошибка в записи файла: {e}")

    def to_sql(self, file_path: str) -> None:
        """Exports data as SQL INSERT statements.
        Экспортирует данные в виде SQL INSERT запросов.

        Args:
            `file_path` (str): Output file path / Путь к файлу"""
        if not self:
            raise ValueError("Нет данных для записи")
        
        try:
            with open(file_path, 'w', encoding='utf-8') as sqlfile:
                columns = ", ".join(self[0].keys())
                sqlfile.write(f"INSERT INTO table_name ({columns})\nVALUES\n")
                for i in range(len(self)):
                    values = ', '.join(f'"{v}"' if isinstance(v, str) else f'{v}' for v in self[i].values())
                    sqlfile.write(f"\t({values}),\n") if i != len(self) - 1 else sqlfile.write(f"\t({values})\n;")
        except OSError as e:
            print(f"Ошибка записи файла: {e}")

    def to_pandas(self):
        """Converts data to pandas DataFrame.
        Конвертирует данные в pandas DataFrame.
        
        Returns:
            DataFrame: Pandas DataFrame object"""
        if not PANDAS_AVAILABLE:
            raise ImportError("Модуль pandas не установлен. Установите его командой: pip install pandas")
        if not self:
            raise ValueError("Нет данных для записи")
        return pd.DataFrame(self)

class DataGenerator:
    """Generates random data based on provided schema.
    Генерирует случайные данные на основе схемы.

    Args:
        `schema` (Table): Table structure definition / Определение структуры таблицы"""
    def __init__(self, schema: Table):
        if not isinstance(schema, Table):
            raise TypeError("Ожидается объект Table")
        self.__schema = schema
        self.__fake = Faker(schema.local)
    
    def generate_data(self, num_rows: int) -> GeneratedData:
        """Generates specified number of data rows.
        Генерирует указанное количество строк данных.

        Args:
            `num_rows` (int): Number of rows to generate / Количество генерируемых строк
            
        Returns:
            GeneratedData: Generated dataset / Сгенерированный набор данных"""
        if num_rows <= 0:
            raise ValueError(f"Число строк должно быть больше 0, сейчас: {num_rows}")
        
        data = []
        for _ in range(num_rows):
            row = {}
            for column, col_type in self.__schema.columns.items():
                if isinstance(col_type, (Job, Phone, Email, Name, Address, Str)):
                    row[column] = col_type.generate(self.__fake)
                else:
                    row[column] = col_type.generate()
            
            data.append(row)
        return GeneratedData(data)