import random
from tablefiller.types import DataType, Int
from tablefiller import DataGenerator, Table

class HexColor(DataType):
    """Генерирует случайный цвет в формате HEX (например, #ff5733)."""
    def generate(self):
        return f"#{random.randint(0, 0xFFFFFF):06x}"

schema = Table(columns={
    "id": Int(3),
    "color": HexColor()
})

generator = DataGenerator(schema)
data = generator.generate_data(5)

print(data.to_pandas())
