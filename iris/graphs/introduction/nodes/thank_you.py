from langchain_core.messages import SystemMessage
from langgraph.graph import MessagesState

from iris.utils.llm import llm


def thank_you(state: MessagesState):
    messages = state["messages"]
    sys_msg = SystemMessage(
        content=(
            "Say thank you to the customer for their interest in the product"
            "and mention that he will be contacted soon"
        )
    )
    response = llm.invoke([sys_msg] + messages)
    return {"messages": response}
