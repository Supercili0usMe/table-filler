import os
import pytest
import pandas as pd
from faker import Faker
from tablefiller import *

# Test data setup (настройки для генерации данных)
@pytest.fixture
def sample_data():
    return [
        {"name": "Test Name", "age": 25, "email": "test@email.com"},
        {"name": "Test Name 2", "age": 30, "email": "test2@email.com"}
    ]

@pytest.fixture
def generated_data(sample_data):
    return GeneratedData(sample_data)

@pytest.fixture
def test_schema():
    return Table({
        'name': Name('both'),
        'age': Int(18, 65),
        'email': Email('email')
    })

# GeneratedData class tests (тесты для сгенерированных данных)
def test_empty_generated_data():
    with pytest.raises(ValueError):
        GeneratedData([]).to_csv('test.csv')

def test_to_csv(generated_data, tmp_path):
    file_path = tmp_path / "test.csv"
    generated_data.to_csv(str(file_path))
    assert os.path.exists(file_path)
    assert os.path.getsize(file_path) > 0

def test_to_json(generated_data, tmp_path):
    file_path = tmp_path / "test.json"
    generated_data.to_csv(str(file_path))
    assert os.path.exists(file_path)
    assert os.path.getsize(file_path) > 0

def test_to_sql(generated_data, tmp_path):
    file_path = tmp_path / "test.sql"
    generated_data.to_csv(str(file_path))
    assert os.path.exists(file_path)
    assert os.path.getsize(file_path) > 0

def test_to_pandas(generated_data):
    df = generated_data.to_pandas()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(generated_data)

def test_invalid_file_path(generated_data):
    with pytest.raises(OSError):
        generated_data.to_csv('invalid/path/test.csv')

# DataGenerator class tests (тесты для генерации данных)
def test_data_generator_init():
    with pytest.raises(TypeError):
        DataGenerator("not a Table object")

def test_generate_data_invalid_rows(test_schema):
    generator = DataGenerator(test_schema)
    with pytest.raises(ValueError):
        generator.generate_data(0)
    with pytest.raises(ValueError):
        generator.generate_data(-1)

def test_generate_data_output(test_schema):
    generator = DataGenerator(test_schema)
    data = generator.generate_data(5)
    assert isinstance(data, GeneratedData)
    assert len(data) == 5
    assert all(isinstance(row, dict) for row in data)
    assert all(key in data[0] for key in test_schema.columns.keys())

def test_generate_data_types(test_schema):
    generator = DataGenerator(test_schema)
    data = generator.generate_data(1)[0]
    assert isinstance(data['name'], str)
    assert isinstance(data['age'], int)
    assert isinstance(data['email'], str)
    assert '@' in data['email']

def test_different_locales():
    schema_en = Table({'name': Name('both')}, local='en_US')
    schema_ru = Table({'name': Name('both')}, local='ru_RU')
    
    gen_en = DataGenerator(schema_en)
    gen_ru = DataGenerator(schema_ru)
    
    data_en = gen_en.generate_data(1)
    data_ru = gen_ru.generate_data(1)
    
    assert data_en[0]['name'] != data_ru[0]['name']

def test_large_data_generation(test_schema):
    generator = DataGenerator(test_schema)
    data = generator.generate_data(1000)
    assert len(data) == 1000
    assert len(set(row['email'] for row in data)) > 900

def test_data_consistency(test_schema):
    generator = DataGenerator(test_schema)
    data = generator.generate_data(10)
    for row in data:
        assert 18 <= row['age'] <= 65
        assert '@' in row['email']
        assert len(row['name'].strip()) > 0