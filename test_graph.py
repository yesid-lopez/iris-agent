from iris.graphs.introduction.graph import graph
from langchain_core.messages import HumanMessage
from langchain_core.messages import HumanMessage


# First message

config = {"configurable": {"thread_id": "92929292"}}
message = HumanMessage("which products do you have?")

for event in graph.stream({"messages": [message]}, config, stream_mode="values", subgraphs=True):
    _, messages = event
    last = messages["messages"][-1]
last.pretty_print()


# Second message
state = graph.get_state(config, subgraphs=True)
graph.update_state(
    state.tasks[0].state.config,
    {
        "messages": [
            HumanMessage(
                content="give me 3 cheese tables and 2 orange juices please!"
            )
        ]
    },
)

for event in graph.stream(None, config, stream_mode="values", subgraphs=True):
    _, messages = event
    last = messages["messages"][-1]
last.pretty_print()
