from tablefiller import DataGenerator, Table
from tablefiller.types import Int, Str, Date, Category

# Create data schema
schema = Table(columns={
    "id": Int(3),
    "name": Str(10),
    "category": Category(["electronics", "clothing", "books"]),
    "created_at": Date("01.01.2022", "31.12.2023")
}, local='en')

# Generate 10 rows
generator = DataGenerator(schema)
data = generator.generate_data(10)

# Show it on console
print(data.to_pandas())

# Save as files
data.to_csv("output.csv")
data.to_json("output.json")
