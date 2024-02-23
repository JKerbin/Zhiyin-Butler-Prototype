import os 
import json

class prompt_generator:
    def __init__(self, config):
        prompt_templates = config.get('conversation', 'prompt_template')
        with open(prompt_templates, 'r', encoding='utf-8') as prompt_file:
            self.prompt_templates = json.load(prompt_file)
        self.default_system_prompt = self.prompt_templates['default_system_prompt']
        self.intention_recognition_prompt = self.prompt_templates['intention_recognition']
        self.chat_intention = self.prompt_templates['chat_intention']
        self.positive_intention = self.prompt_templates['positive_intention']
        self.negative_intention = self.prompt_templates['negative_intention']

    def add_system_prompt_to_conversation(self, conversation):
        system_input = dict()
        system_input['role'] = 'system'
        system_input['content'] = self.default_system_prompt
        conversation.insert(0, system_input)
        return conversation

    def generate_intention_detection_prompt(self, user_input, task_list):
        '''
            :param task_list list[dict]
        '''
        prompt = self.intention_recognition_prompt
        prompt = prompt.replace('<user_input>', user_input)
        task_list_str = ''
        for idx, task in enumerate(task_list):
            task_list_str += (str(idx + 1) + '. ' + task['task_description']) + ' '
        task_list_str  += str(len(task_list) + 1) + '.' + self.chat_intention + ' '
        prompt = prompt.replace('<task_list>', task_list_str)
        return prompt

    def generate_verification_prompt(self, user_input):
        prompt = self.intention_recognition_prompt
        prompt = prompt.replace('<user_input>', user_input)
        choice_list_str = ''
        choice_list_str += ('1.' + self.positive_intention)
        choice_list_str += ('2.' + self.negative_intention)
        prompt = prompt.replace('<task_list>', choice_list_str)
        return prompt

    def generate_params_filling_prompt(self, user_input, task):
        prompt = task['template']
        prompt = prompt.replace('<user_input>', user_input)
        return prompt
        

        

    