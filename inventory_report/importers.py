from typing import Dict, Type
import abc
from inventory_report.product import Product
import json


class Importer(abc.ABC):
    def __init__(self, path: str):
        self.path = path

    @abc.abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, 'r') as file:
            data = json.load(file)
            result = []
            for product in data:
                product = Product(**product)
                result.append(product)

        return result


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
