class Table:
    def __init__(self, columns: dict, local: str ='ru_RU'):
        """Создание схемы таблицы.
        ----
        Параметры:
            - `columns` - словарь используемых столбцов в исходной таблице. Пример создания столбца: `'name': Name('both')`
            - `local` - определение локали для генерации данных. По умолчанию 'ru_RU'"""
        if not columns:
            raise ValueError("Схема таблицы не может быть пустой")
        self.columns = columns
        self.local = local