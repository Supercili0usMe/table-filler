from tablefiller import DataGenerator, Table
from tablefiller.types import Int, Str, Date

schema = Table(columns={
    "id": Int(4, 15),
    "username": Str(8),
    "registered_at": Date("01.01.2020", "01.01.2024")
})

generator = DataGenerator(schema)
data = generator.generate_data(5)

# Save SQL-file
data.to_sql("output.sql")

# Show SQL commands
with open("output.sql", "r") as f:
    print(f.read())
