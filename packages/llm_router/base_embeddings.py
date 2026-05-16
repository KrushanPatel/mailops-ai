class BaseEmbeddingProvider:

    def generate_embedding(self, text: str):
        raise NotImplementedError
