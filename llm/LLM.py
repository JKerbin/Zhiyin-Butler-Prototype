from abc import abstractmethod

class LLM:
    @abstractmethod
    def __init__(self, config):
        pass

    @abstractmethod
    def load(self):
        pass 

    @abstractmethod
    def chat_async(self, conversation):
        pass 

    @abstractmethod
    def chat_sync(self, conversation):
        pass