from typing import TypedDict

from langgraph.graph import MessagesState

from iris.models.order import Order
from iris.models.product import Product


class OrderState(TypedDict, MessagesState):
    products: list[Product]
    order: Order
    should_order: bool
