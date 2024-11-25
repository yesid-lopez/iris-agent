from langchain_core.messages import SystemMessage

from iris.graphs.product.states.product_state import ProductState
from iris.services.product_service import get_products
from iris.utils.llm import llm


def show_products(state: ProductState):
    messages = state["messages"]
    products = get_products()
    prompt = (
        "Consider the following products available: "
        f"{products} to give an answer to the customer."
        "considering the product"
    )
    response = llm.invoke([SystemMessage(prompt)] + messages)
    return {"products": products, "messages": response}
