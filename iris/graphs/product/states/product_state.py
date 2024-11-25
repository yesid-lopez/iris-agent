from typing import TypedDict

from langgraph.graph import MessagesState

from iris.models.product import Product


class ProductState(TypedDict, MessagesState):
    products: list[Product]
    