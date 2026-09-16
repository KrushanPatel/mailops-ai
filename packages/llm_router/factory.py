from langchain.chat_models import init_chat_model
from langchain.embeddings import init_embeddings

from packages.llm_router.settings import llm_settings


def get_chat_provider():

    kwargs = {}

    if llm_settings.CHAT_API_KEY:
        kwargs["api_key"] = llm_settings.CHAT_API_KEY

    if llm_settings.CHAT_BASE_URL:
        kwargs["base_url"] = llm_settings.CHAT_BASE_URL

    return init_chat_model(
        model=llm_settings.CHAT_MODEL,
        model_provider=llm_settings.CHAT_PROVIDER,
        **kwargs
    )


def get_embedding_provider():

    kwargs = {}

    if llm_settings.EMBEDDING_API_KEY:
        kwargs["api_key"] = llm_settings.EMBEDDING_API_KEY

    if llm_settings.EMBEDDING_BASE_URL:
        kwargs["base_url"] = llm_settings.EMBEDDING_BASE_URL

    return init_embeddings(
        llm_settings.EMBEDDING_MODEL, provider=llm_settings.EMBEDDING_PROVIDER, **kwargs
    )
