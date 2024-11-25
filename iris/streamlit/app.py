import streamlit as st
from langchain_core.messages import HumanMessage

from iris.clients.directus_client import DirectusClient
from iris.graphs.introduction.graph import graph
from uuid import uuid4

# Initialize thread ID and conversation state
if "thread_id" not in st.session_state:
    st.session_state.thread_id = uuid4()  # Fixed thread ID for simplicity

# Display thread ID
st.markdown(f"**Thread ID:** {st.session_state.thread_id}")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What products do you offer?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        config = {"configurable": {"thread_id": st.session_state.thread_id}}
        message = HumanMessage(prompt)

        state = graph.get_state(config=config, subgraphs=True)
        if state.next and state.next[0] == "product":
            subgraph_state = state.tasks[0].state
            state = graph.update_state(
                subgraph_state.config,
                {"messages": [HumanMessage(content=prompt)]}
            )
        else:
            graph.update_state(
                config,
                {"messages": [HumanMessage(content=prompt)]},
            )
        for event in graph.stream(None, config, stream_mode="values", subgraphs=True):
            _, messages = event
            message = messages["messages"][-1]

        response = st.write(message.content)
        state = graph.get_state(config=config, subgraphs=True)

        if state.next and state.next[0] == "product":
            products = state.tasks[0].state.values["products"]
            columns = st.columns(len(products))
            for product, col in zip(products, columns):
                with col:
                    image_stream = DirectusClient().get_image(product.image)
                    st.image(image_stream, caption=product.name, width=150)
        st.session_state.messages.append(
            {"role": "assistant", "content": message.content})
