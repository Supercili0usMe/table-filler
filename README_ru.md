# Table-Filler 🏗️  

**Table-Filler** — это библиотека для генерации тестовых данных в SQL-таблицы, JSON и CSV. 

## Установка 📦  
```sh
pip install tablefiller
```
Или установите последнюю версию из GitHub:
```sh
pip install git+https://github.com/Supercili0usMe/table-filler.git
```

## Быстрый старт 🚀  
```python
from tablefiller import DataGenerator, Table
from tablefiller.types import Int, Str, Date

schema = TableSchema(columns={
    "id": Int(5, 10),
    "name": Str(10),
    "created_at": Date("01.01.2022", "31.12.2023", '%d.%m.%Y')
}, local="ru_RU")

generator = DataGenerator(schema)
data = generator.generate_data(5)

print(data.to_pandas())  # Вывод в DataFrame
data.to_csv("output.csv")  # Сохранение в CSV
```

## Возможности 🎯  
✔️ Генерация чисел, строк, дат, категорий  
✔️ Faker (имена, адреса, email)  
✔️ Экспорт в **CSV, JSON, SQL**  
✔️ Поддержка **pandas.DataFrame**  
✔️ Кастомные типы  

## Доступные типы данных 🏗️  
| Тип                | Описание                                     |
| ------------------ | -------------------------------------------- |
| `Int(a, b)`        | Целое число от `a` до `b`                    |
| `Float(a, b, d)`   | Число с `d` знаками после `.`                |
| `Str(n)`           | Строка длиной `n`                            |
| `Date(start, end)` | Случайная дата в диапазоне                   |
| `Category([...])`  | Категория из списка                          |
| `Job("type")`      | Данные из Faker (`male`, `female`, `both`)   |
| `Phone()`          | Данные из Faker                              |
| `Email("type")`    | Данные из Faker (`email`, `free`, `company`) |
| `Name("type")`     | Данные из Faker (`male`, `female`, `both`)   |
| `Address("type")`  | Данные из Faker (`street`, `city`, `full`)   |

## Экспорт данных 📤  
```python
data.to_csv("output.csv")  # CSV
data.to_json("output.json")  # JSON
data.to_sql("output.sql")  # SQL
```

## Создание своих типов данных 🔧  
```python
import random
from table_filler.types import DataType

class HexColor(DataType):
    def generate(self):
        return f"#{random.randint(0, 0xFFFFFF):06x}"

schema = TableSchema(columns={"id": Int(1, 3), "color": HexColor()})
```

## Тестирование ✅  
```sh
pytest tests/
```

## Лицензия 📜  
**MIT License**
