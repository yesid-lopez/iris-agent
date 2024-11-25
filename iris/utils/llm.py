import os
from iris.utils.model_wrappers.langchain_chat_models import ChatSambaNovaCloud

sambanova_api_key = os.getenv("SAMBANOVA_API_KEY")

llm = ChatSambaNovaCloud(
    model="Meta-Llama-3.1-70B-Instruct",
    temperature=0,
    sambanova_url="https://api.sambanova.ai/v1/chat/completions",
    sambanova_api_key=sambanova_api_key,
)
