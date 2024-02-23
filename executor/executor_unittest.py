import unittest
from configparser import ConfigParser
from executor import executor

class ExecutorTestingClass(unittest.TestCase):
    def generate_config(self):
        test_config = ConfigParser()
        test_config.add_section('executor')
        test_config.set('executor', 'task_list', 'config\\task_list.json')
        test_config.set('executor', 'scripts_path', 'config\scripts')
        test_config.set('executor', 'tmp_path', 'tmp\\')
        return test_config

    def test_executor(self):
        config = self.generate_config()
        e = executor(config)
        e.set_current_task(2)
        e.generate_script_using_params({'<params1>':'5', '<params2>':'50'})
        e.excute()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

    