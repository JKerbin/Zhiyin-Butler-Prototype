from conversation.conversation import conversation 
from llm.ChatGPT import GPT 
from executor.executor import executor
from conversation.prompt_generator import prompt_generator
import json

class conversation_manager:
    def __init__(self, config):
        self.executor = executor(config)
        self.prompt_generator = prompt_generator(config)
        self.llm = GPT(config)
        self.llm.load()
        self.conversation = conversation()

    def deal_with_input(self, input_text):

        self.conversation.add_conversation('user', input_text)
        if self.executor.current_task_id is not None:
            vertification_prompt = self.prompt_generator.generate_verification_prompt(input_text)
            vertification = dict()
            vertification['role'] = 'user'
            vertification['content'] = vertification_prompt 
            prompt = self.prompt_generator.add_system_prompt_to_conversation([vertification,])
            response = self.llm.chat_sync(prompt)
            if response == '1':
                self.executor.excute()
            self.executor.set_current_task(None)
            return '执行完毕。'
        
        else:
            intention_recognition_prompt = self.prompt_generator.generate_intention_detection_prompt(input_text, self.executor.task_list)
            intention_recognition = dict()
            intention_recognition['role'] = 'user'
            intention_recognition['content'] = intention_recognition_prompt
            prompt = self.prompt_generator.add_system_prompt_to_conversation([intention_recognition,])
            response = int(self.llm.chat_sync(prompt))

            if response == len(self.executor.task_list) + 1:
                response = self.llm.chat_sync(self.prompt_generator.add_system_prompt_to_conversation(self.conversation.get_llm_input_format()))
                self.conversation.add_conversation('assistant', response)
                return response
            else:
                self.executor.set_current_task(response)
                if self.executor.task_list[self.executor.current_task_id - 1]['require_extra_params']:
                    params_filling_prompt = self.prompt_generator.generate_params_filling_prompt(input_text, self.executor.task_list[self.executor.current_task_id - 1])
                    params_filling = dict()
                    params_filling['role'] = 'user'
                    params_filling['content'] = params_filling_prompt
                    params = self.llm.chat_sync(self.prompt_generator.add_system_prompt_to_conversation([params_filling]))
                    self.executor.generate_script_using_params(json.loads(params))
                return '您确定要执行该命令吗？'