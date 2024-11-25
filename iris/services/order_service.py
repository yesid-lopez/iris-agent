from langchain_core.tools import tool

from iris.clients.directus_client import DirectusClient
from iris.models.order import Order


@tool()
def create_order(order: Order):
    """Creates orders considering that one order can have several items
    
    Args:
        order (Order): The order to create
    """
    return DirectusClient().create_order(order.model_dump())
