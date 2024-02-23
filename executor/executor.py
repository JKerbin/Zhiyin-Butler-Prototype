import json
import os

class executor:
    def __init__(self, config):
        task_list = config.get('executor', 'task_list')
        self.task_list = json.load(open(task_list, 'r', encoding='utf-8'))
        self.scripts_path = config.get('executor', 'scripts_path')
        self.current_task_id = None
        self.current_task_script = ''
        self.tmp_script_path = config.get('executor', 'tmp_path')

    def set_current_task(self, task_id):
        self.current_task_id = task_id
        if task_id is None:
            self.current_task_script = None
            return
        current_task_script_path = os.path.join(self.scripts_path, self.task_list[task_id - 1]['excutable_file'])
        with open(current_task_script_path, 'r', encoding='utf-8') as f:
            self.current_task_script = f.read()
    
    def generate_script_using_params(self, params):
        for key, value in params.items():
            self.current_task_script = self.current_task_script.replace(key, str(value))
        assert(not( '<' in self.current_task_script and '>' in self.current_task_script))

    def excute(self):
        tmp_script_file = os.path.join(self.tmp_script_path, 'tmp.bat')
        with open(tmp_script_file, 'w', encoding='utf-8') as f:
            f.write(self.current_task_script)
        os.system(self.current_task_script)