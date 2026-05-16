class BaseChatProvider:

    def generate(self, prompt: str):
        raise NotImplementedError
