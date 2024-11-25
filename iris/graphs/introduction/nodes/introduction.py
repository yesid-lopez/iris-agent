from pydantic import BaseModel, Field

from iris.enums.category import CategoryEnum
from iris.graphs.introduction.states.customer_service_state import \
    CustomerServiceState
from iris.utils.llm import llm


class Introduction(BaseModel):
    category: CategoryEnum = Field(
        description="Category of the customer service")
    intention: str = Field(description="Intention of the customer service")


def intro(state: CustomerServiceState):
    messages = state["messages"]
    llm_struct = llm.with_structured_output(schema=Introduction)
    intro = llm_struct.invoke(messages)
    return {"category": intro.category, "intention": intro.intention}
