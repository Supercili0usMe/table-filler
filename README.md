# Table-Filler 🏗️  

**Table-Filler** is a library for generating test data for SQL tables, JSON, and CSV. 

## Installation 📦  
```sh
pip install tablefiller
```
Or install the latest version from GitHub:
```sh
pip install git+https://github.com/Supercili0usMe/table-filler.git
```

## Quick Start 🚀  
```python
from tablefiller import DataGenerator, TableSchema
from tablefiller.types import Int, Str, Date

schema = TableSchema(columns={
    "id": Int(5, 10),
    "name": Str(10),
    "created_at": Date("01.01.2022", "31.12.2023", '%d.%m.%Y')
}, local="en_EN")

generator = DataGenerator(schema)
data = generator.generate_data(5)

print(data.to_pandas())  # Output to DataFrame
data.to_csv("output.csv")  # Save to CSV
```

## Features 🎯  
✔️ Generate numbers, strings, dates, and categories  
✔️ Faker support (names, addresses, emails)  
✔️ Export to **CSV, JSON, SQL**  
✔️ **pandas.DataFrame** support  
✔️ Сustom data types  

## Available Data Types 🏗️  
| Type               | Description                             |
| ------------------ | --------------------------------------- |
| `Int(a, b)`        | Integer from `a` to `b`                 |
| `Float(a, b, d)`   | Number with `d` decimal places          |
| `Str(n)`           | String of length `n`                    |
| `Date(start, end)` | Random date within range                |
| `Category([...])`  | Category from a list                    |
| `Job("type")`      | Faker data (`male`, `female`, `both`)   |
| `Phone()`          | Faker data                              |
| `Email("type")`    | Faker data (`email`, `free`, `company`) |
| `Name("type")`     | Faker data (`male`, `female`, `both`)   |
| `Address("type")`  | Faker data (`street`, `city`, `full`)   |

## Data Export 📤  
```python
data.to_csv("output.csv")  # CSV
data.to_json("output.json")  # JSON
data.to_sql("output.sql")  # SQL
```

## Creating Custom Data Types 🔧  
```python
import random
from table_filler.types import DataType

class HexColor(DataType):
    def generate(self):
        return f"#{random.randint(0, 0xFFFFFF):06x}"

schema = TableSchema(columns={"id": Int(3), "color": HexColor()})
```

## Testing ✅  
```sh
pytest tests/
```

## License 📜  
**MIT License**