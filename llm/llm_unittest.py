import unittest
from configparser import ConfigParser
from ChatGPT import GPT
OpenAI_API_KEY = ''

def generate_chatgpt_config(openai_api_key):
    '''
        针对ChatGPT相关的单元测试生成一个configparser对象
        :param openai_key 一个OpenAI的api_key
    '''
    test_config = ConfigParser()
    test_config.add_section('llm')
    test_config.set('llm', 'api_key', openai_api_key)
    return test_config


class LLMTestingClass(unittest.TestCase):
    def test_ChatGPT_sync(self):
        config = generate_chatgpt_config(OpenAI_API_KEY)
        chatgpt = GPT(config)
        try:
            chatgpt.load()
        except BaseException as e:
            print('Client creation failed')
            self.assertTrue(False)
        finally:
            pass

        openai_response = chatgpt.chat_sync([
        {
            "role": "user",
            "content": "Say this is a test",
        }])

        if type(openai_response) == str and len(openai_response) > 0:
            self.assertTrue(True)

        self.assertFalse(False)

    def test_ChatGPT_async(self):
        config = generate_chatgpt_config(OpenAI_API_KEY)
        chatgpt = GPT(config)
        try:
            chatgpt.load()
        except BaseException as e:
            print('Client creation failed')
            self.assertTrue(False)
        finally:
            pass

        openai_response = chatgpt.chat_async([
        {
            "role": "user",
            "content": "Say this is a test",
        }])

        for part in openai_response:
            print(part.choices[0].delta.content or "")


if '__main__' == __name__:
    unittest.main()