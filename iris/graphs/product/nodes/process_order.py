from langchain_core.messages import SystemMessage
from pydantic import BaseModel, Field

from iris.graphs.product.states.product_state import ProductState
from iris.models.order import Order
from iris.services.order_service import create_order
from iris.utils.llm import llm


class OrderStructure(BaseModel):
    order: Order
    order_finished: bool = Field(
        description="Whether to create the order or not")


process_order_tools = [create_order]


def process_order(state: ProductState):
    messages = state["messages"]
    llm_tools = llm.bind_tools(tools=process_order_tools)

    sys_msg = SystemMessage(
        f"Considering the products: {state["products"]}"
        "You are a customer service assistant tasked to create an order"
        "considering what the customer wanted to buy"
    )
    response = llm_tools.invoke([sys_msg] + messages)
    return {"messages": [response]}
