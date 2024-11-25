from typing import TypedDict

from langgraph.graph import MessagesState

from iris.enums.category import CategoryEnum


class CustomerServiceState(TypedDict, MessagesState):
    category: CategoryEnum
    intention: str
