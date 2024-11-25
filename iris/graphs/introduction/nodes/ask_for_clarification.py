from langchain_core.messages import SystemMessage

from iris.enums.category import CategoryEnum
from iris.graphs.introduction.states.customer_service_state import (
    CustomerServiceState,
)
from iris.utils.llm import llm

def ask_for_clarification(state: CustomerServiceState):
    messages = state["messages"]
    if state["category"] == CategoryEnum.other:
        sys_msg = SystemMessage(
            content=(
                "Clarify to the customer if he wants to do one of the following actions:"
                "1. Buy a product"
                "2. Return a product"
                ""
            )
        )
        return {"messages": llm.invoke([sys_msg] + messages)}
