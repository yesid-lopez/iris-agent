from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, MessagesState, StateGraph

from iris.graphs.product.nodes.get_products import show_products
from iris.graphs.product.nodes.process_order import process_order, process_order_tools
from langgraph.prebuilt import tools_condition, ToolNode

product_builder = StateGraph(MessagesState)


# Add Nodes
product_builder.add_node("show_products", show_products)
product_builder.add_node("process_order", process_order)
product_builder.add_node("tools", ToolNode(process_order_tools))

# Add Edges
product_builder.add_edge(START, "show_products")
product_builder.add_edge("show_products", "process_order")
product_builder.add_conditional_edges(
    "process_order",
    tools_condition,
)
product_builder.add_edge("tools", END)

memory = MemorySaver()
product_graph = product_builder.compile(
    interrupt_after=["show_products"],
)
