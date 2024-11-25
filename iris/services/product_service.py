from iris.clients.directus_client import DirectusClient
from iris.models.product import Product


def get_products() -> list[Product]:
    products_json = DirectusClient().get_products()
    products = [Product(**product) for product in products_json]
    return products
