from langgraph.graph import END

from iris.enums.category import CategoryEnum
from iris.graphs.introduction.states.customer_service_state import (
    CustomerServiceState,
)


def should_continue(state: CustomerServiceState):
    category = state["category"]
    if category == CategoryEnum.other:
        return "ask_for_clarification"
    if category == CategoryEnum.product:
        return "product"
    return END
