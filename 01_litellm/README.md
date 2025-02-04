## LiteLLM Python SDK

[Docs](https://docs.litellm.ai/docs/#litellm-python-sdk)

CrewAI has transitioned to using LiteLLM for integrating with various Large Language Models (LLMs). LiteLLM serves as an intermediary, allowing CrewAI to connect seamlessly with multiple LLM providers. This approach offers flexibility in choosing the appropriate model for specific use cases.

Despite this shift, CrewAI maintains compatibility with LangChain tools. You can continue to integrate LangChain’s comprehensive set of tools into your CrewAI agents to enhance their capabilities.

In summary, while CrewAI now utilizes LiteLLM for LLM integrations, it still supports the use of LangChain tools within its framework.

LiteLLM is a Python SDK designed to simplify interactions with over 100 Large Language Models (LLMs) from various providers, including OpenAI, Anthropic, VertexAI, HuggingFace, Azure OpenAI, Ollama, and OpenRouter. It offers a unified interface, consistent output formatting, and built-in retry and fallback mechanisms, making it an invaluable tool for developers working with multiple LLMs.