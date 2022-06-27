from os import environ
from logging import INFO, getLogger
from dataclasses import asdict

from dynamo_databases import DynamoDatabase # CommonLayer

from lib.models import Product

logger = getLogger()
logger.setLevel(INFO)

class ProductsTable(DynamoDatabase):

    def __init__(self):
        super().__init__(environ.get("PRODUCTS_TABLE_NAME"), "Name", "Id")

    def save(self, products: list[Product]) -> None:
        logger.info(f"Saving the following products {products} to Products table ...")
        self._put(items=[asdict(product) for product in products])
        logger.info("Finished saving products!")

    def get(self) -> list[Product]:
        pass

    def update(self):
        pass

    def delete(self):
        pass
