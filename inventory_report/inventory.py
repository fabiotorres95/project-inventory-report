from typing import Optional
from inventory_report.product import Product


class Inventory:
    def __init__(self, data: Optional[list[Product]] = None):
        self.__data = data if data else []

    def __str__(self) -> str:
        return f"{self.data}"

    @property
    def data(self) -> list[Product]:
        return self.__data

    def add_data(self, data: list[Product]) -> None:
        self.__data.extend(data)
