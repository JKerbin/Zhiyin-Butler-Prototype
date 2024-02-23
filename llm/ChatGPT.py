from llm.LLM import LLM
from openai import OpenAI


class GPT(LLM):
    def __init__(self, config):
        self.config = config 
        self.client = None

    def load(self):
        try:
            self.client = OpenAI(api_key=self.config['llm']['api_key'])
        except BaseException as excetpion:
            return excetpion

    def chat_sync(self, conversation):
        chat_completion = self.client.chat.completions.create(
        messages=conversation, model="gpt-3.5-turbo")
        return chat_completion.choices[0].message.content

    def chat_async(self, conversation):
        stream = self.client.chat.completions.create(model="gpt-3.5-turbo",
    messages=conversation, stream=True)
        return stream
