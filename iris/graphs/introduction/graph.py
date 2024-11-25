from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, MessagesState, StateGraph

from iris.graphs.introduction.nodes.ask_for_clarification import ask_for_clarification
from iris.graphs.introduction.nodes.introduction import intro
from iris.graphs.introduction.nodes.thank_you import thank_you
from iris.graphs.introduction.nodes.should_continue import should_continue
from iris.graphs.product.graph import product_graph

entry_builder = StateGraph(MessagesState)

# Add Nodes
entry_builder.add_node("introduction", intro)
entry_builder.add_node("ask_for_clarification", ask_for_clarification)
entry_builder.add_node("product", product_graph)
entry_builder.add_node("thank_you", thank_you)

# Add Edges
entry_builder.add_edge(START, "introduction")
entry_builder.add_conditional_edges(
    "introduction",
    should_continue,
    ["ask_for_clarification", "product", END],
)
entry_builder.add_edge("ask_for_clarification", "introduction")
entry_builder.add_edge("product", "thank_you")
entry_builder.add_edge("thank_you", END)


memory = MemorySaver()
graph = entry_builder.compile(
    interrupt_after=["ask_for_clarification"],
    checkpointer=memory,
)
